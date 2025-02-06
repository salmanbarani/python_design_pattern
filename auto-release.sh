#!/bin/bash

# Function to extract the current version from setup.py
get_version_from_setup() {
    grep 'version=' setup.py | sed -E 's/.*version="([^"]+)".*/\1/'
}

# Get the latest tag from the repository
latest_tag=$(git describe --tags --abbrev=0 2>/dev/null)

# Get the version from setup.py
setup_version=$(get_version_from_setup)

# Function to compare version numbers
version_greater() {
    # Compare two version numbers
    if [ "$(printf '%s\n' "$1" "$2" | sort -V | head -n1)" != "$1" ]; then
        return 0
    else
        return 1
    fi
}

# Check if there is a tag
if [ -z "$latest_tag" ]; then
    echo "No tags found. Creating a new tag with version $setup_version from setup.py."
    git tag -a "v$setup_version" -m "Release version $setup_version"
    echo "READY TO RELEASE"
    #TODO: Release the tag 
    echo "Released Successfully, ready to push the newly created tag"
    git push origin "v$setup_version" --verbose
    echo "Pushed Successfully"
else
    echo "Latest tag found: $latest_tag"
    # Compare the setup.py version with the latest tag
    if version_greater "$setup_version" "${latest_tag#v}"; then
        echo "Version $setup_version from setup.py is greater than the latest tag $latest_tag."
        echo "Creating a new tag with version $setup_version."
        git tag -a "v$setup_version" -m "Release version $setup_version"
        echo "READY TO RELEASE"
        #TODO: Release the tag 
        echo "Released Successfully, ready to push the newly created tag"
        git push origin "v$setup_version" --verbose
        echo "Pushed Successfully"
    else
        echo "No new tag created. The version in setup.py ($setup_version) is not greater than the latest tag ($latest_tag)."
    fi
fi
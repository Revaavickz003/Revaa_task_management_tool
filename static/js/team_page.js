// show roles

document.addEventListener('DOMContentLoaded', (event) => {
    const mainCheckboxes = document.querySelectorAll('.main-checkbox');

    mainCheckboxes.forEach(checkbox => {
        checkbox.addEventListener('change', function() {
            const subContainer = this.closest('.form-check').querySelector('.sdccontainer');
            const subCheckboxes = subContainer.querySelectorAll('.form-check-input');
            const subLabels = subContainer.querySelectorAll('.form-check-label');

            // Hide all sub-content containers and uncheck all checkboxes inside them
            document.querySelectorAll('.sdccontainer').forEach(container => {
                container.style.display = 'none';
                container.querySelectorAll('.form-check-input').forEach(subCheckbox => {
                    subCheckbox.checked = false;
                });
                container.querySelectorAll('.form-check-label').forEach(subLabel => {
                    subLabel.style.display = 'none';
                });
            });


            // Uncheck all main checkboxes and hide them
            mainCheckboxes.forEach(cb => {
                const parentCheck = cb.closest('.form-check');
                if (cb !== this) {
                    cb.checked = false;
                    parentCheck.style.display = 'none';
                } else {
                    parentCheck.style.display = 'block';
                    parentCheck.querySelector('.form-check-label').style.display = 'block'; // Show the heading of the checked checkbox
                }
            });

            // If the current checkbox is checked, show its sub-content container and labels
            if (this.checked) {
                subContainer.style.display = 'block';
                subLabels.forEach(label => {
                    label.style.display = 'block';
                });
            } else {
                // Show all main checkboxes if none is checked
                mainCheckboxes.forEach(cb => {
                    cb.closest('.form-check').style.display = 'block';
                    cb.closest('.form-check').querySelector('.form-check-label').style.display = 'block'; // Show the heading of the unchecked checkbox
                });
            }
        });
    });
});


// Show sub container

document.addEventListener('DOMContentLoaded', function() {
    document.querySelectorAll('.dot-button').forEach(function(button) {
        button.addEventListener('click', function() {
            var optionsList = button.nextElementSibling;
            optionsList.classList.toggle('show');
        });
    });

    document.addEventListener('click', function(event) {
        document.querySelectorAll('.options-list').forEach(function(optionsList) {
            if (!optionsList.previousElementSibling.contains(event.target) && !optionsList.contains(event.target)) {
                optionsList.classList.remove('show');
            }
        });
    });
});


// Show drap down

function toggleDropdown(event, dropdownId) {
    event.stopPropagation();
    const options = document.getElementById(dropdownId);
    options.classList.toggle("show");
}

window.onclick = function(event) {
    if (!event.target.closest('.dropdown')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

document.querySelectorAll('.dropdown-content input[type="checkbox"]').forEach(checkbox => {
    checkbox.addEventListener('change', function() {
        const selectedTagsContainer = checkbox.closest('.dropdown').querySelector('.selected-tags');
        let selectedValues = Array.from(checkbox.closest('.dropdown-content').querySelectorAll('input[type="checkbox"]:checked'))
                                  .map(cb => ({id: cb.value, name: cb.getAttribute('data-name')}));
        updateSelectedTags(selectedValues, selectedTagsContainer);
    });
});

function updateSelectedTags(selectedValues, container) {
    container.innerHTML = '';
    selectedValues.forEach(value => {
        const tag = document.createElement('div');
        tag.className = 'tag';
        tag.innerHTML = `<span>${value.name}</span><span class="remove-tag" onclick="removeTag('${value.id}', this)">x</span>`;
        container.appendChild(tag);
    });
}

function removeTag(id, element) {
    const checkbox = element.closest('.dropdown').querySelector(`input[value="${id}"]`);
    if (checkbox) {
        checkbox.checked = false;
        const selectedTagsContainer = checkbox.closest('.dropdown').querySelector('.selected-tags');
        let selectedValues = Array.from(checkbox.closest('.dropdown-content').querySelectorAll('input[type="checkbox"]:checked'))
                                  .map(cb => ({id: cb.value, name: cb.getAttribute('data-name')}));
        updateSelectedTags(selectedValues, selectedTagsContainer);
    }
}

function filterOptions(searchId, dropdownId) {
    const searchInput = document.getElementById(searchId).value.toLowerCase();
    const labels = document.getElementById(dropdownId).querySelectorAll('label');

    labels.forEach(label => {
        const text = label.textContent.toLowerCase();
        if (text.includes(searchInput)) {
            label.style.display = "";
        } else {
            label.style.display = "none";
        }
    });
}

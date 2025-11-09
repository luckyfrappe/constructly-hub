const banner = document.querySelector(".banner");
const deleteButtons = document.getElementsByClassName("btn-delete");
const deleteConfirm = document.getElementById("deleteConfirm");

if (banner) {
  const closeButton = banner.querySelector("button");
  closeButton.addEventListener("click", () => {
    banner.style.display = "none";
  });
}

/**
 * Adds real-time validation styling to all form inputs.
 * 
 * For every input element on the page:
 * - Removes the "wrong-field" class when the user starts typing or changing the value.
 * - Reapplies the "wrong-field" class if the field becomes empty again.
 * 
 * This gives instant visual feedback during form interaction.
 */
 const inputs = document.querySelectorAll("input, textarea, select, textfield");

inputs.forEach((input) => {
  input.addEventListener("input", () => {
    // Remove red border on typing
    input.classList.remove("wrong-field");

    // Find all .wrong-text elements in the same parent <div>
    const wrongTexts = input.parentElement.querySelectorAll(".wrong-text");
    wrongTexts.forEach((el) => (el.style.display = "none"));

    // If the field becomes empty again → reapply red border
    if (input.value.trim() === "") {
      input.classList.add("wrong-field");
    }
  });
});

/**
* Initializes deletion functionality for the provided delete buttons.
* 
* For each button in the `deleteButtons` collection:
* - Retrieves the associated comment's ID upon click.
* - Updates the `deleteConfirm` link's href to point to the 
* deletion endpoint for the specific comment.
* - Displays a confirmation modal (`deleteModal`) to prompt 
* the user for confirmation before deletion.
*/
for (let button of deleteButtons) {
  button.addEventListener("click", (e) => {
    let companyId = e.target.getAttribute("data-company_id");
    deleteConfirm.href = `delete_company/${companyId}`;
  });
}
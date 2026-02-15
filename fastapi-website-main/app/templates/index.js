fetch("/students")
  .then((r) => r.json())
  .then((data) => {
    let container = document.getElementById("data");
    data.forEach((s) => {
      container.innerHTML += `
                            <div class="card">
                                <h2>${s.name}</h2>
                                <div class="info-item"><span class="label">Hobby:</span> <br>${s.hobby || "保密"}</div>
                                <div class="info-item"><span class="label">Age:</span> ${s.age || "100"}</div>
                                <div class="info-item"><span class="label">Favorite Color:</span> ${s.color || "Secret"}</div>
                                <div class="info-item"><span class="label">About Me:</span> ${s.biography || "Secret"}</div>
                                <div class="info-item"><span class="label">Contact:</span> ${s.socials || "Secret"}</div>
                            </div>
                        `;
    });
  });

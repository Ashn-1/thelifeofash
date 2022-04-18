
function load_sidebar(url)
{
    fetch(url)
        .then(function (response) 
        {
            return response.json();  
        })
        .then(function (data) 
        {
            var sidebar_container = document.getElementById("sidebar");
            for (var i = 0; i < data.length; i++)
            {
                var bold = document.createElement("b");
                /*
                if (data[i]["category"] == "daily")
                {
                    bold.innerHTML = "D ";
                } else {
                    bold.innerHTML = "A ";
                }
                */

                var span = document.createElement("span");
                span.appendChild(bold);
                span.innerHTML += data[i]["title"];

                var link = document.createElement("a");
                link.setAttribute("href", data[i]["url"]);
                link.setAttribute("class", "sidebar-item grey-link");
                link.appendChild(span);  
                
                sidebar_container.appendChild(link);
            }
        })
        .catch(function (err) 
        {
            console.log("Could not fetch " + url);
            console.log("Error: " + err);
        });
}

edit_time();
setInterval(() => edit_time())
function edit_time() {
    const time = document.getElementById("time");
    const timezone = document.getElementById("time-zone");
    const date = new Date();
    const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
    const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    const info = formatDate(date);
    time.innerHTML = `${info.time}`;
    timezone.innerHTML = `${info.tz}`
    function formatDate(d) {
        const time = d.toLocaleString().split(", ")[1];
        const month = months[d.getMonth()];
        const dotw = days[d.getDay()];
        let day = d.getDate().toString();
        if (day.endsWith("1") && !day.endsWith("11")) day += "st";
        else if (day.endsWith("2") && !day.endsWith("12")) day += "nd";
        else if (day.endsWith("3") && !day.endsWith("13")) day += "rd";
        else day += "th";
        let offset = new Date().getTimezoneOffset(), offabs = Math.abs(offset);
        let tz = Intl.DateTimeFormat().resolvedOptions().timeZone;
        let tz_ = "UTC" + (offset < 0 ? "+" : "-") + Math.floor(offabs / 60) + (offabs % 60 ? ":" + ("00" + (offabs % 60)).slice(-2) : "");
        return { time: `${time}, ${dotw} ${day} ${month} ${d.getYear() + 1900}`, tz: `${tz} - ${tz_}` }
    }
}

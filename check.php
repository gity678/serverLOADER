<?php
// بيانات التفعيل (ممكن تخزينها بقاعدة بيانات لاحقًا)
$codes = [
    "vip2025" => true,
    "test123" => true,
    "premium777" => true
];

// استقبال الكود من التطبيق
$code = $_GET['code'] ?? '';

// سجل الوصول
file_put_contents("log.txt", date("Y-m-d H:i:s") . " - CODE: $code\n", FILE_APPEND);

// التحقق
if (isset($codes[$code])) {
    echo json_encode(["status" => "ok"]);
} else {
    echo json_encode(["status" => "fail"]);
}
?>

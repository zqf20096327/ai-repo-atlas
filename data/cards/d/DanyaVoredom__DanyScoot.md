# DanyaVoredom/DanyScoot

⭐ 3 · Kotlin · MIT · 推送 2026-10-26 · [GitHub](https://github.com/DanyaVoredom/DanyScoot) · 个人维护

**控制 Urent 滑板车与 Edifier 耳机的 Android BLE 工具，带 AI 助手**

Android 应用（包名 ru.dany.scoot，最低 Android 6.0），通过 BLE 连接使用 Nordic UART 协议的 Urent 电动滑板车及 Edifier 耳机：支持 GATT 扫描连接、密钥握手、解锁/锁定/寻车/灯光等命令、遥测读取、54 个操作码目录与任意 hex 命令发送。内置 AI 助手支持 OpenAI Chat Completions/Responses 与 Anthropic Messages 三种接口，可调用 BLE 工具执行扫描、连接、读写特征值等操作。协议依据 references 目录中的参考 APK 逆向还原；README 注明未经真实硬件验证，密钥与 API key 以明文存储于 SharedPreferences。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 支持 Urent 滑板车解锁/锁定/遥测等 54 个操作码命令
- AI 助手可调用 BLE 工具（扫描/连接/读写特征/发送命令）
- 兼容 Edifier 耳机与任意标准 GATT 设备
- 支持 OpenAI 与 Anthropic 三种 API 格式并自动识别

## 适用场景

- 扫描并连接 Nordic UART 协议的 BLE 滑板车发送控制命令
- 读取滑板车遥测数据与 GATT 服务转储
- 通过对话让 AI 助手代为执行 BLE 操作
- 管理 Edifier 耳机的服务与电量信息

## 场景标签

 · 领域:IoT/硬件工具

## 证据(README 行号)

> L3: Android-приложение для BLE-устройств: электросамокаты Urent с Nordic UART и гарнитуры Edifier. Протокол самоката вос
> L88: - AI-ассистент: OpenAI Chat Completions, OpenAI Responses, Anthropic Messages, автоопределение формата, история, ос
> L134: - Сеть используется для AI-запросов и проверки обновлений. Команды самоката по-прежнему выполняются только по BLE.


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `0eaa766a1127` · [字段定义](../../DATASET.md)*

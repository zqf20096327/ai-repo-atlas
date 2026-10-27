# AmarnathCJD/ApexClaw

⭐ 25 · Go · MIT · 推送 2026-06-24 · [GitHub](https://github.com/AmarnathCJD/ApexClaw) · 个人维护

**Telegram 个人 AI 助手：GLM 驱动、100+ 内置工具的 agent**

运行在 Telegram 上的个人 AI 代理，由 GLM 模型驱动，内置 100+ 工具：图像分析、语音转录、WhatsApp/Gmail/日历集成、无头浏览器自动化、文件与系统操作、长期记忆与 TF-IDF 知识库、定时任务等。用 Go 编写，提供 curl 一键安装脚本（下载二进制并引导配置 Telegram 凭据）或从源码构建。附带可选的本地 Web 仪表盘（localhost:8080，JWT 认证）。依赖 Go 1.22+、ffmpeg（语音）与 Chrome/Chromium（浏览器自动化）。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 100+ 内置工具，覆盖系统执行、浏览器自动化、邮件日历、媒体下载等
- 长期记忆：键值事实存储与 TF-IDF 排序的可搜索知识库
- curl 一键安装脚本下载二进制并启动交互式配置向导
- 可选 Web 仪表盘管理设置与查看日志（localhost:8080）

## 适用场景

- 在 Telegram 中通过对话让 agent 代为收发邮件、管理日程
- 语音消息转文字并触发工具执行
- 让 agent 用无头浏览器浏览网页、下载视频、查询数据

## 场景标签

`AI 助手` `浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L7: **Your personal AI assistant that lives in Telegram.** Not just a chatbot—a capable agent that thinks, uses tools, a
> L9: Apexclaw is powered by GLM and comes with **100+ built-in tools** covering everything from file management and web a

## 星数曲线

```mermaid
xychart-beta
    title "AmarnathCJD/ApexClaw 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-27 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 high · 依据 README sha `32a08e31a255` · [字段定义](../../DATASET.md)*

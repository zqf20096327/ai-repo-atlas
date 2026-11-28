# avonxate-hub/wca-ai-tool-s12-MI6

⭐ 3 · Python · 推送 2026-11-27 · [GitHub](https://github.com/avonxate-hub/wca-ai-tool-s12-MI6) · 个人维护

**面向小店主的 AI 库存管理与补货建议对话工具**

基于 Google Gemini API 的命令行库存咨询应用：店主逐条报告库存、销售与补货问题，应用维护多轮对话记忆，要求 AI 返回结构化 JSON（message/priority/recommendations）并做字段校验，失败自动重试一次；会话结束时生成摘要并连同完整对话保存为本地 JSON 文件，可从主菜单回看历史会话。API key 经 .env 文件管理，需 Python 3 与网络连接。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多轮对话记忆，后续问题可引用先前消息
- 结构化 JSON 响应校验与失败自动重试
- 会话摘要生成与本地 JSON 存档回看
- .env 管理 API key，密钥不入库

## 适用场景

- 记录小店每日库存并查询剩余量
- 向 AI 询问是否需要补货并获取建议
- 回看历史会话了解库存问题脉络

## 场景标签

`聊天机器人` · 领域:对话与助手

## 证据(README 行号)

> L3: Duka Stock Advisor is an AI-powered stock management assistant designed to help small shop and duka owners monitor i
> L5: The application uses the Google Gemini API and maintains conversation history throughout a session so that the AI ca


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `ea1336fd8699` · [字段定义](../../DATASET.md)*

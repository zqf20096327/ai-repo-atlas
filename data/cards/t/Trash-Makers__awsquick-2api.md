# Trash-Makers/awsquick-2api

⭐ 10 · Python · MIT · 推送 2026-11-23 · [GitHub](https://github.com/Trash-Makers/awsquick-2api) · 个人维护 · 中文 README

**把 AWS Quick 对话能力转为 OpenAI 兼容接口的本地网关**

awsquick-2api 是一个本地运行的网关，将 AWS Quick（原 Amazon QuickSight）的对话能力转换为 OpenAI Chat Completions 协议，客户端通过 base_url 即可接入。支持流式输出、多账号轮询、401/403/429/5xx 自动切号、指数退避、额度熔断、qk_ 前缀密钥分发与按小时/模型/账号的成本账本。自带 Flask 控制台，八页面管理账号池、密钥、调用明细，数据本地存储。附带可选注册机（半自动/手动邮箱池/全自动框架），需自配收信方式；README 声明仅供个人学习与技术研究，需自行确认符合 AWS 服务条款。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- OpenAI 兼容端点 /v1/models 与 /v1/chat/completions，支持流式
- 多账号轮询与 401/403/429/5xx 自动切号，指数退避+半开探测
- 额度熔断、qk_ 密钥分发、逐笔成本账本
- Flask 控制台八页面，数据全部本地存储

## 适用场景

- 让只支持 OpenAI 协议的客户端直接调用 AWS Quick 的对话能力
- 管理多个账号的免费额度，超额自动熔断
- 本地记录每次调用的模型、tokens 与成本

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L13: `awsquick-2api` 是一个本地网关。它把 AWS Quick（原 Amazon QuickSight）的对话能力，转换成标准的 OpenAI Chat Completions 协议：
> L25: - **OpenAI 兼容**：`/v1/models`、`/v1/chat/completions`，支持流式
> L46: │ 你的应用      │ ───────────────▶ │  网关 :3426      │


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-24 · 置信度 high · 依据 README sha `c8c982875eef` · [字段定义](../../DATASET.md)*

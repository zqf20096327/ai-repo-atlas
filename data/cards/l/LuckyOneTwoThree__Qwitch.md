# LuckyOneTwoThree/Qwitch

⭐ 5 · Rust · MIT · 推送 2026-11-26 · [GitHub](https://github.com/LuckyOneTwoThree/Qwitch) · 组织维护 · 中文 README

**给多账号 AI 工具用户的本地账号管理与号池网关**

本地优先的桌面应用（Tauri v2 + Rust），用于管理多个 AI 订阅工具账号：内置 7 个账号适配器（Trae CN、WorkBuddy、Qoder CN、MiniMax Code CN、LobsterAI、豆包工作、码道 CodeArts）加通用 API Key，提供额度/签到查看与领取、事务式桌面登录切换，并在本机 127.0.0.1:8187 启动网关，支持 OpenAI Chat/Responses 与 Anthropic Messages 三种协议转换，把订阅账号按号池规则接入 Codex、Claude、DSH、OpenCode、MiMo、ZCode 等客户端。凭据 AES-256-GCM 加密存本机；不提供云端同步、团队共享或批量注册，自动化默认关闭。macOS/Windows 提供安装包，均未签名。

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

- 7 个内置账号适配器均通过 Rust 原生上游协议接入本地网关
- 本地网关支持 OpenAI Chat、OpenAI Responses、Anthropic Messages 三种协议互转，含流式与工具调用
- 同工具多账号组成号池，按主备顺序、剩余额度、轮询选择，429 冷却、401 刷新 Token、熔断保护
- 账号与凭据本机 SQLite 存储，AES-256-GCM 加密，主密钥存系统钥匙串

## 适用场景

- 同时管理多个 AI 订阅工具的额度、签到与登录状态
- 把订阅账号接到 Codex/Claude 等多个 Agent 客户端复用
- 同一工具多账号轮流调用，按额度自动主备切换
- 本机保存凭据与路由日志，不依赖云端

## 场景标签

`模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L113: **本地网关。** 一个只监听 `127.0.0.1:8187` 的小服务，支持 OpenAI Chat、OpenAI Responses 和 Anthropic Messages 三种主流接口格式，并能在它们之间转换。Agen
> L115: **Agent 接入。** Qwitch 直接修改 Codex、Claude、DSH、OpenCode、MiMo、ZCode 的配置文件，把网关地址、令牌和模型清单写进去。修改前会备份，解绑时会还原。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-27 · 置信度 high · 依据 README sha `6cd767d866f7` · [字段定义](../../DATASET.md)*

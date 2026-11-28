# hongfaqiu/rokbot

⭐ 69 · JavaScript · NOASSERTION · 推送 2026-11-27 · [GitHub](https://github.com/hongfaqiu/rokbot) · [官网](https://rokbot.cosfoc.com) · 个人维护 · 中文 README

**自托管私有 AI 助手：六端接入，数据与模型自管**

部署在自己服务器上的 AI 助手 Host，配套网页、macOS、Windows、Linux、安卓与 iOS 六端客户端。对话、文件、配置与 API Key 存本地数据卷，全端关闭遥测；兼容 OpenAI Chat Completions/Responses 与 Anthropic Messages 协议，支持 6 个场景的模型路由与每路最多 8 个备用模型自动切换。提供内置 Linux 桌面容器（VNC 查看接管）、画布托管、用量报表、多 Bot 群聊与 rokbot 命令行部署工具。采用 Docker Compose 部署，许可为非商业许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 兼容 OpenAI 与 Anthropic 协议，6 个场景模型路由、每路最多 8 个备用模型
- 六端客户端连接同一 Host，6 位配对码接入、无需云端账号
- 内置 Linux 桌面容器供 Bot 操作，VNC 实时查看与接管
- rokbot 命令行：部署、环境检查、更新回滚、本地打包

## 适用场景

- 在自有服务器上部署私有 AI 助手，数据不出本机
- 从 Grok Bot 迁移 Bot、记忆与技能到自托管环境
- 让 Bot 在容器或本机执行命令并实时查看操作过程
- 多个 Bot 组群协作并统计各 Bot 用量

## 场景标签

`AI 助手` `模型网关` · 领域:Agent 开发

## 证据(README 行号)

> L5:  部署在你自己服务器上的私有 AI 助手：数据留在本地，模型自己选，网页、桌面和手机随时接力。
> L33: - **模型自己选**：兼容 OpenAI Chat Completions、OpenAI Responses 和 Anthropic Messages，接哪家服务、用哪个模型由你决定。
> L46: - **六端覆盖**：网页、Mac、Windows、Linux（x64 / arm64）、安卓和 iOS 连同一台 Host，电脑上布置的任务可以在手机上接着看。


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `71ccdee00d6a` · [字段定义](../../DATASET.md)*

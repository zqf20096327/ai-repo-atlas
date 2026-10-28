# DeadMeme5441/arrodes

⭐ 29 · Clojure · MIT · 推送 2026-10-27 · [GitHub](https://github.com/DeadMeme5441/arrodes) · 个人维护

**围绕持久 Clojure REPL 的终端编程 agent**

在终端中运行的编程 agent：以一个持久 Clojure REPL 为核心求值器，模型调用以普通函数组合方式执行，原生值在步骤间保留；会话、结果与项目配置存放在仓库之外（~/.arrodes），不在项目内创建配置文件。支持多 provider 账号接入（含 Codex/ChatGPT 登录、Anthropic OAuth 与 API key），提供模型浏览、会话分支、后台任务、HTML 导出与 JSON Lines RPC 无头模式。提供 macOS 与 glibc Linux 的自包含二进制，Windows 支持为实验性且未包含在发布中；运行的是受信任本地代码而非沙箱。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 持久 Clojure REPL 保留原生值，函数调用可在会话中检查
- 会话持久化、分支与重启恢复；项目状态不写入仓库
- 多 provider 接入与模型/推理等级切换，支持 OAuth 与 API key
- arrodes --rpc 提供版本化 JSON Lines API 供自动化集成

## 适用场景

- 在终端里让 agent 解释、修复并验证项目中的问题
- 以持久 REPL 状态逐步迭代 Clojure 项目代码
- 通过 RPC 模式把 agent 嵌入自动化流程

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: Arrodes is a terminal coding agent built around a persistent Clojure REPL. The agent composes ordinary functions and
> L93: On first run, the **Providers** browser opens. Connect an account, browse its models,
> L212: For automation and integrations, the only headless terminal mode is:

## 星数曲线

```mermaid
xychart-beta
    title "DeadMeme5441/arrodes 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-26", "2026-10-28"]
    y-axis "stars" 26 --> 30
    line [27, 28, 29, 29]
```

2026-10-18 27 → 2026-10-28 29（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `08467d0a8de5` · [字段定义](../../DATASET.md)*

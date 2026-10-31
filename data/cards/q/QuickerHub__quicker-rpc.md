# QuickerHub/quicker-rpc

⭐ 14 · TypeScript · MIT · 推送 2026-10-28 · [GitHub](https://github.com/QuickerHub/quicker-rpc) · [官网](https://github.com/QuickerHub/quicker-rpc/blob/main/docs/quicker-agent.md) · 组织维护 · 中文 README

**Quicker 的 AI 桌面副驾与无头动作 RPC 工具集**

面向 Windows 效率工具 Quicker 的 monorepo，含三件东西：QuickerAgent（终端用户 AI 助手，描述用途即搜索/执行/编辑动作，全局快捷键唤起）、QuickerRpc 插件（在 Quicker 进程内通过命名管道 + StreamJsonRpc 托管 RPC 服务）、qkrpc CLI（供开发者与第三方 Agent 以 CLI/MCP/HTTP 无头读写动作，支持 Cursor 等宿主一键接入）。限定 Windows 10 1607+/.NET 10 体系，V2 原生 MCP 编辑有来源显式启用等限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 命名管道 + StreamJsonRpc 统一底层，CLI 连插件内 RPC 服务
- qkrpc 提供 CLI/MCP/HTTP 三种无头通道，支持 --json 输出
- qkrpc agent setup 为 Cursor 等第三方 Agent 一键配置 MCP 与 skills
- QuickerAgent 内置动作编辑器与步骤知识库，全局启动器（默认 Ctrl+Shift+Space）

## 适用场景

- 用自然语言查找、运行、修改我的 Quicker 动作
- 在 Cursor / Claude / VS Code 里通过 MCP 无头编辑 Quicker 动作
- 脚本或 CI 中用 qkrpc CLI/HTTP 调用 Quicker 动作

## 场景标签

`AI 助手` · 领域:对话与助手

## 证据(README 行号)

> L9: |**QuickerAgent**|Quicker 终端用户|桌面 AI 副驾：找 / 跑 / 改 / 发动作，全局快捷键秒开|
> L13: 底层统一：**命名管道 + StreamJsonRpc**，CLI 作客户端连插件内的 `IQuickerRpcService`。
> L28: 专为 Quicker 打造的 AI 助手：内置动作编辑器与步骤知识库，描述用途即可搜索执行，复杂编排进主窗口，轻量操作走可配置的全局启动器（默认 **Ctrl+Shift+Space**）。

## 星数曲线

```mermaid
xychart-beta
    title "QuickerHub/quicker-rpc 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 high · 依据 README sha `d6b185ef712d` · [字段定义](../../DATASET.md)*

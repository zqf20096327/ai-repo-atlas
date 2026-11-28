# heurica-labs/anvil

⭐ 49 · Swift · AGPL-3.0 · 推送 2026-11-27 · [GitHub](https://github.com/heurica-labs/anvil) · [官网](https://heurica.dev) · 组织维护

**原生 macOS 编码代理应用：描述改动即自动探索、编辑、运行测试**

基于 SwiftUI 的原生 Mac 编码代理，用户描述改动后自动探索仓库、编辑代码、运行测试并修复问题，所有编辑以 diff 形式呈现供审查。与多数代理调用模型原生 tool-calling API 不同，其使用自定义纯文本协议（模型在回复中批量给出 JSON 动作），减少往返轮次与 token 开销，可在任意聊天模型上运行。提供 Ask/Auto-accept/Plan only/Bypass 四种权限模式、每请求检查点回退、第二模型审查 diff、失败后切换模型家族等机制。要求 macOS 15+ 与 Xcode 26+，目前无签名发行版，需从源码构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 纯文本协议批量动作：一次回复读多文件、做多次编辑并跑测试，减少往返
- 任意 OpenAI 兼容 API 接入，另支持 ChatGPT/Gemini 网页账号登录
- 子会话在独立 git worktree 并行运行并支持冲突检查合并
- 语法/LSP 检查、done 前跑测试、第二调用审查 diff

## 适用场景

- 描述一个 bug 或功能，让代理在本地仓库自动完成修改和测试
- 把一个特性拆成子会话在多个 worktree 并行开发后合并
- 通过 headless CLI 在脚本和评测中运行编码代理

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L17: Anvil is a native Mac coding agent in the spirit of Claude Code and Codex, built with SwiftUI. Describe a change an
> L7: 5x faster and 12x cheaper than opencode on the same model. 1 A native Mac app that reads, edits, runs and tests unti


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-28 · 置信度 high · 依据 README sha `a7b63523db54` · [字段定义](../../DATASET.md)*

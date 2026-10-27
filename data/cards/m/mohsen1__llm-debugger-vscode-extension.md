# mohsen1/llm-debugger-vscode-extension

⭐ 361 · TypeScript · MIT · 推送 2026-09-21 · [GitHub](https://github.com/mohsen1/llm-debugger-vscode-extension) · 个人维护

**VSCode 扩展：LLM 驱动真实调试器逐步定位并修复 bug**

VSCode 调试扩展，通过驱动真实调试器（设断点、单步、读取运行时变量值）让 LLM 定位 bug，而非仅读源码。每步路由由 Jev（System One 分类模型）决定，生成模型（默认 gpt-5.4-nano）仅在需要断点位置、表达式与最终补丁时调用，附 13 任务基准判定补丁是否真正修复。需配置 OPENAI_API_KEY 与 TYPESAFE_API_KEY；通过 VSIX 或源码开发方式安装。作者声明其为概念验证研究实验，非受支持产品。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 驱动真实调试器（断点/单步/活体变量）而非静态读码
- Jev 分类路由 + 生成模型按需调用的混合模式
- 13 任务基准：以补丁应用且测试通过判定解决
- 暴露 8 个 agent 可调用调试工具，支持 MCP（Claude Code/Codex CLI）

## 适用场景

- 让 AI 在真实运行时中定位测试失败的根因并给出补丁
- 在 VSCode 聊天侧栏用 @debugger 狩猎指定 bug
- 供 Copilot/Claude Code 等 agent 通过工具调用活体调试器

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A VSCode extension that finds bugs by *running* the code — driving the real
> L31: Traditional LLM-based debugging approaches analyze only static source code. With LLM Debugger, the LLM is provided 
> L222: The live debugger is exposed as eight agent-callable tools, so another agent can

## 星数曲线

```mermaid
xychart-beta
    title "mohsen1/llm-debugger-vscode-extension 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 360 --> 362
    line [361, 361]
```

2026-10-18 361 → 2026-10-27 361（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 high · 依据 README sha `6744cd662596` · [字段定义](../../DATASET.md)*

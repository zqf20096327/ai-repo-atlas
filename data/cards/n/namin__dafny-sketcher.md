# namin/dafny-sketcher

⭐ 18 · Dafny · MIT · 推送 2026-07-31 · [GitHub](https://github.com/namin/dafny-sketcher) · 个人维护

**给 Dafny 用户的交互式半自动验证程序合成工具**

基于 Dafny 语言实现（fork 的 dafny 与 ide-vscode 子模块）构建的验证程序合成探索工具，结合 LLM 与符号推理，为引理自动生成归纳案例分析等证明骨架。提供 VSCode 扩展、CLI、MCP 与 VFP 测试床四种使用途径。LLM 为可选配置，支持 Anthropic/Gemini API key 或默认假定本地 Ollama 可用。需从源码编译（compile.sh、dotnet、npm），核心是 Dafny: Generate Sketch 命令，默认自动检测归纳变量，可用 {:induction_on} 覆盖。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 结合 LLM 与符号推理为 Dafny 引理生成归纳案例分析等证明骨架
- 提供 VSCode 扩展、CLI、MCP、VFP 四种使用方式
- LLM 可选：支持 Anthropic/Gemini key 或默认假定 Ollama 可用
- 归纳变量默认自动检测，可用 {:induction_on} 覆盖

## 适用场景

- 在 VSCode 里为不能自动验证的 Dafny 引理生成证明骨架
- 通过 CLI 或 MCP 在工作流中调用 sketcher
- 研究 LLM 与符号推理结合的验证程序合成

## 场景标签

`代码生成` · 领域:编码与开发

## 证据(README 行号)

> L2: piggybacking on the Dafny language implementation to explore interactive semi-automated verified program synthesis, 
> L4: Besides the dev setup to use Dafny Sketcher in a VSCode extension, Dafny Sketcher is available through a CLI, an MCP

## 星数曲线

```mermaid
xychart-beta
    title "namin/dafny-sketcher 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 17 --> 19
    line [18, 18]
```

2026-10-18 18 → 2026-10-30 18（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-29 · 置信度 high · 依据 README sha `36ccfc1f0f0c` · [字段定义](../../DATASET.md)*

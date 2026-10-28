# arthurpanhku/j7scope

⭐ 21 · Python · Apache-2.0 · 推送 2026-10-28 · [GitHub](https://github.com/arthurpanhku/j7scope) · 个人维护 · 中文 README

**检验语言模型内部 J-space 跨语言共享性的研究项目与实时旁路工具**

两项内容共存的仓库：一是独立复现并扩展 Anthropic 的全局工作空间（J-space）研究，用 J-lens 读出中间层残差流，检验中英文语境触发的概念方向是否共享（H1/H2/H3 三个假设，M1 相关性/M2 activation patching/M3 分级验证的方法路线）；二是 j7scope-serve 旁路——一个 OpenAI 兼容代理，插在 agent harness（opencode/codex 等）与自托管开源模型之间，实时逐 token 显示模型“倾向说但未说”的概念，中英两列。闭源 API 不暴露激活故无法读出。研究侧自述处于早期脚手架阶段，M1 尚无结论性数据；hf 后端待 GPU 验证。提供零依赖 mock 后端、静态 Gallery 站与 Colab 采集 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | `cpu-ok` | |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | `idea` | |

## 能力要点

- J-lens 读出中间层残差流，逐 token 显示模型未说出的概念
- OpenAI 兼容代理旁路，可接 opencode/codex 等任意 harness
- 跨语言严谨层：null 基线、sharedness 置信区间、CKA 统计陷阱处理
- mock 后端纯标准库零依赖，可无 GPU 跑通整条链路

## 适用场景

- 我用 opencode/codex 驱动本地开源模型时，实时观察其内部概念读出
- 研究中英双语下模型全局工作空间是否共享同一套概念表示
- 录制并回放 trace，导出跨语言对齐证据（SVG/PNG/JSON/BibTeX）

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L23: 1. **一项研究** —— 独立复现并扩展 Anthropic 的全局工作空间（J-space）研究，检验模型内部的"思维空间"在中英双语下是否共享同一套概念表示。这是一个大部分可解释性研究者做不了的双语视角实验。（见 §4 研
> L26: 研究是内核，旁路是它的可见化应用。**旁路不需要研究结论成立就能跑** —— 它本身就是一个"看模型在想什么"的工具。
> L31: ┌──────────────┐   OpenAI /v1/chat/completions    ┌────────────────────────┐

## 星数曲线

```mermaid
xychart-beta
    title "arthurpanhku/j7scope 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-28 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 mid · 依据 README sha `514c6fa113f2` · [字段定义](../../DATASET.md)*

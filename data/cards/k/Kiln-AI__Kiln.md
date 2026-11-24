# Kiln-AI/Kiln

⭐ 5,292 · Python · NOASSERTION · 推送 2026-11-24 · [GitHub](https://github.com/Kiln-AI/Kiln) · [官网](https://kiln.tech) · 组织维护

**团队协作构建、评估与优化 AI 系统的本地工作台**

Kiln 提供覆盖 AI 开发全流程的工作台：评估（evals）、prompt 优化、RAG、子代理编排、合成数据生成与零代码微调，同一任务与数据集可在各阶段复用。桌面应用供 PM、领域专家与 QA 无代码参与打标和评分，MIT 许可的 Python 库将相同任务发布到生产环境，并与 Git 同步协作。本地优先运行，可用自带 API key 或通过 Ollama 离线运行；桌面应用为 source-available 的 fair-code 模式。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Eval Builder 自动生成评估器与合成评估数据集
- 拖拽文档（PDF/图像/视频/音频）创建 RAG 并自动生成评估
- 60+ 模型零代码微调，支持 Fireworks/Together/Vertex 部署
- 同一 MIT 库同时供桌面应用与生产部署使用

## 适用场景

- 为我的任务搭建评估集并对比 prompt/模型改动的质量回归
- 让团队非工程成员参与数据打标与输出评分
- 为微调快速生成合成训练数据
- 把应用中构建的 agent 通过 Python 库部署到生产

## 场景标签

`提示工程` `模型评测` `RAG` `微调` · 领域:Agent 开发

## 证据(README 行号)

> L30: Kiln is a workbench for the full AI development loop: evals, optimization, prompts, RAG, fine-tuning, synthetic dat
> L46: - 🎛️ **Fine-Tuning** - Zero-code fine-tuning across 60+ models (Qwen, Llama, GPT, Gemini, …) on Fireworks, Together
> L82: Build AI tasks in the app. Deploy with the open-source library. Same engine, same project files, no rewrite. The MI

## 星数曲线

```mermaid
xychart-beta
    title "Kiln-AI/Kiln 星数(近 25 点)"
    x-axis ["2026-10-22", "2026-10-23", "2026-10-24", "2026-10-25", "2026-10-26", "2026-10-27", "2026-10-28", "2026-10-29", "2026-10-30", "2026-10-31", "2026-11-01", "2026-11-06", "2026-11-08", "2026-11-10", "2026-11-12", "2026-11-13", "2026-11-14", "2026-11-15", "2026-11-16", "2026-11-18", "2026-11-20", "2026-11-21", "2026-11-22", "2026-11-23", "2026-11-24"]
    y-axis "stars" 5207 --> 5296
    line [5214, 5224, 5226, 5229, 5232, 5235, 5237, 5242, 5245, 5246, 5247, 5229, 5264, 5267, 5272, 5273, 5280, 5281, 5284, 5286, 5287, 5285, 5286, 5289, 5289]
```

2026-10-22 5,214 → 2026-11-24 5,289（+75）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-22 · 置信度 high · 依据 README sha `b45463109e55` · [字段定义](../../DATASET.md)*

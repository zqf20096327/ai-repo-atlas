# ninjahawk/Subtext

⭐ 246 · HTML · NOASSERTION · 推送 2026-07-23 · [GitHub](https://github.com/ninjahawk/Subtext) · 个人维护

**实时可视化语言模型内部工作区的机制可解释性仪器**

基于 Anthropic 的 Jacobian lens 方法，在与本地模型（默认 Qwen3.5-4B）对话的同时，对每个 token 在 9 个层深读取残差流激活，经 J_l 传输与 unembedding 解码为词汇倾向，实时渲染到浏览器画布，并配 per-token 台账、逐词检查器、trace 视图与可回放会话导出。面向机制可解释性研究者与爱好者，需要 NVIDIA GPU（约 10GB 显存）或 Apple Silicon（16GB+）运行，回放无需 GPU。限制：仅能读出对应单词元的概念。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 对话中逐 token 读取 9 层深度的 lens 读出并实时渲染
- prefill 阅读阶段 + KV cache 生成阶段均覆盖，流式达模型原生生成速度
- verify_accuracy.py 对照参考实现：top-5 读出完全一致，logit 余弦相似度 ≥ 0.99998
- 会话可导出为 JSON，任意浏览器无 GPU 回放

## 适用场景

- 观察模型在生成前内部已形成的判断与计划
- 复现论文中的 two-hop 中间项等报告/规划现象
- 为其他 HuggingFace decoder 自行拟合 lens 后做同类观察

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L27: Recent work from Anthropic identified a small set of internal representations in
> L37: Subtext applies that method continuously during live conversation with a local
> L85: - **Each rendered word is a lens readout, not model output.** It indicates an

## 星数曲线

```mermaid
xychart-beta
    title "ninjahawk/Subtext 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 245 --> 248
    line [246, 247, 247]
```

2026-10-18 246 → 2026-10-22 247（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-22 · 置信度 mid · 依据 README sha `680e67c483a4` · [字段定义](../../DATASET.md)*

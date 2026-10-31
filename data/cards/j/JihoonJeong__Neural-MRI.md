# JihoonJeong/Neural-MRI

⭐ 16 · Python · MIT · 推送 2026-04-10 · [GitHub](https://github.com/JihoonJeong/Neural-MRI) · [官网](https://jihoonjeong.github.io/Neural-MRI/) · 个人维护

**LLM 内部机制可视化诊断工具，如脑部 MRI 般扫描模型**

面向可解释性研究的 Web 应用：输入开源 LLM 与 prompt，以五种仿医学影像的扫描模式（T1 架构、T2 权重、fMRI 激活、DTI 信息流、FLAIR 异常检测）可视化模型内部。基于 TransformerLens 与 SAE-Lens，提供扰动引擎（消融/放大并测 KL 散度）、因果追踪、情绪向量提取与行为引导、跨模型对比，支持 WebSocket 逐 token 流式展示与 WebM/GIF/JSON 导出。前端 React+D3，后端 FastAPI+PyTorch，通过 HuggingFace Hub 动态加载 TransformerLens 兼容模型，模型规模受 GPU 显存限制。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 5 种扫描模式覆盖架构、权重、激活、信息流与异常检测
- 扰动引擎与因果追踪（KL 散度、逐层恢复分数）
- SAE 特征分析（SAELens + EleutherAI 双后端）
- 情绪向量提取与模型行为引导（20 种情绪）

## 适用场景

- 研究者对开源 LLM 做机制可解释性分析
- 检测模型内部偏置与异常模式
- 对比两个模型在同一 prompt 下的内部激活差异

## 场景标签

`科研工具` `模型评测` · 领域:评测与运维

## 证据(README 行号)

> L10: Neural MRI Scanner visualizes the internals of open-source LLMs like a **brain MRI** — mapping five medical imaging
> L115: |Backend|FastAPI, TransformerLens, PyTorch, SAE-Lens, EleutherAI Sparsify|

## 星数曲线

```mermaid
xychart-beta
    title "JihoonJeong/Neural-MRI 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 15 --> 17
    line [16, 16]
```

2026-10-18 16 → 2026-10-31 16（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `d3af5fead5d9` · [字段定义](../../DATASET.md)*

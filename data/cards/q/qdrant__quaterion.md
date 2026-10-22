# qdrant/quaterion

⭐ 665 · Python · Apache-2.0 · 推送 2026-10-05 · [GitHub](https://github.com/qdrant/quaterion) · [官网](https://quaterion.qdrant.tech/) · 组织维护

**面向语义搜索等任务的相似度学习模型微调框架**

基于 PyTorch Lightning 的相似度学习微调框架，用于语义搜索、推荐、异常检测、极端分类与匹配引擎等场景的模型训练。通过内置缓存机制支持大批量多轮训练（README 称可在笔记本 GPU 上运行），配合预训练模型与专用 head 层适配小数据集。分为 quaterion（训练）与 quaterion-models（推理）两个 pip 包，推理端可避免安装重型训练依赖；框架各部分均可重定义，支持 ONNX 格式导出。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 内置缓存机制，支持大 batch 多 epoch 训练
- 基于 PyTorch Lightning 构建，继承其扩展能力
- 训练包与推理包分离（quaterion / quaterion-models）
- 提供 head 层 skip connection、embedding 置信度、向量坍缩防止等特性教程

## 适用场景

- 为自己的语义搜索或推荐任务微调相似度模型
- 只有小规模标注数据时基于预训练模型做特化
- 在推理服务端以轻量依赖部署微调后的模型

## 场景标签

`语义搜索` `微调` `推荐系统` · 领域:知识与检索

## 证据(README 行号)

> L12: Quaterion is a framework for fine-tuning similarity learning models.
> L27: * 🌌 **Scalable**: Quaterion is built on top of PyTorch Lightning and inherits all its scalability, cost-efficiency,

## 星数曲线

```mermaid
xychart-beta
    title "qdrant/quaterion 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-22"]
    y-axis "stars" 663 --> 666
    line [664, 665, 665]
```

2026-10-18 664 → 2026-10-22 665（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `ddcc687ff7af` · [字段定义](../../DATASET.md)*

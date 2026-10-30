# ahmetkumass/yolo-gen

⭐ 41 · Python · MIT · 推送 2026-04-21 · [GitHub](https://github.com/ahmetkumass/yolo-gen) · 个人维护

**从 YOLO 标签自动生成 VLM 训练数据的一体化训练管线**

面向视觉开发者的训练工具：用一条命令在标准 YOLO 数据集上依次训练目标检测模型和微调视觉语言模型。核心机制是从既有 YOLO 标注自动生成 VLM 问答对（描述模式或 Yes/No 验证模式），并通过环形候选搜索加 DINOv2 相似度过滤实现免检测器的困难负样本挖掘，含 IoU 排除等多层防泄漏保护。支持 Qwen-VL、InternVL、GLM-4.6V-Flash 等模型族，默认 4-bit QLoRA 训练并导出 ONNX。限制：需 Python 3.10+，VLM 训练 VRAM 需 14-28 GB。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 从 YOLO 标签自动生成描述式或 Yes/No 验证式 VLM 训练数据
- 免检测器的困难负样本挖掘：环形搜索 + DINOv2 相似度过滤，含多层防泄漏保护
- 支持 Qwen2.5-VL/Qwen3-VL/InternVL 3.5/GLM-4.6V-Flash，默认 4-bit QLoRA
- 单 YAML 配置驱动，含 --skip-yolo 等模块化跳过参数

## 适用场景

- 在缺陷检测、武器检测、医学影像等场景中训练 YOLO+VLM 两级检测管线
- 微调 VLM 用于验证检测框、过滤误检
- 无需额外标注就把既有 YOLO 数据集转成 VLM 训练数据

## 场景标签

`目标检测` `微调` · 领域:感知与多模态

## 证据(README 行号)

> L8: Image + YOLO labels → Auto-generate VLM training data → Fine-tuned model
> L101: All VLMs train with 4-bit QLoRA + LoRA by default; the per-family
> L152: python train.py --config configs/my_run.yaml

## 星数曲线

```mermaid
xychart-beta
    title "ahmetkumass/yolo-gen 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 40 --> 42
    line [41, 41]
```

2026-10-18 41 → 2026-10-30 41（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `9bc691060d1e` · [字段定义](../../DATASET.md)*

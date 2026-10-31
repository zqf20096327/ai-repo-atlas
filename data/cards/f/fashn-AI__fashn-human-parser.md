# fashn-AI/fashn-human-parser

⭐ 61 · Python · NOASSERTION · 推送 2026-01-10 · [GitHub](https://github.com/fashn-AI/fashn-human-parser) · [官网](https://fashn.ai/) · 组织维护

**时尚/虚拟试穿用人体解析库：输出 18 类语义分割掩码**

基于 SegFormer-B4（MIT-B4 编码器 + MLP 解码器）的人体解析模型包，针对时尚与虚拟试穿场景微调，输出 18 类语义分割掩码（脸、发、上衣、裙、裤等）。首次使用时权重（约 244 MB）从 HuggingFace Hub 下载并本地缓存。提供一行式 predict API，接受文件路径/PIL/NumPy 输入，支持批处理与返回原始 logits，预处理与训练时一致；也可经 HuggingFace pipeline 直接调用。许可继承 NVIDIA SegFormer 源码许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | NOASSERTION |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- SegFormer-B4 输出 18 类人体语义分割掩码，掩码尺寸与输入一致
- predict 支持文件路径/PIL/NumPy 输入与单次前向批量处理
- 包内使用与训练一致的预处理（cv2.INTER_AREA），可返回原始 logits
- 导出 IDENTITY_LABELS、CATEGORY_TO_BODY_COVERAGE 等虚拟试穿相关映射

## 适用场景

- 虚拟试穿应用中分割人体与服装区域
- 时尚图像分析中获取服装类别掩码
- 批量处理图像生成 18 类语义分割图

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L6: A SegFormer-B4 model fine-tuned for human parsing with 18 semantic classes, optimized for fashion and virtual try-on
> L103: - **Architecture**: SegFormer-B4 (MIT-B4 encoder + MLP decoder)

## 星数曲线

```mermaid
xychart-beta
    title "fashn-AI/fashn-human-parser 星数(近 4 点)"
    x-axis ["2026-10-18", "2026-10-25", "2026-10-30", "2026-10-31"]
    y-axis "stars" 58 --> 62
    line [59, 60, 61, 61]
```

2026-10-18 59 → 2026-10-31 61（+2）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `102731d937bf` · [字段定义](../../DATASET.md)*

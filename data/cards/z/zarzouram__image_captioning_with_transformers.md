# zarzouram/image_captioning_with_transformers

⭐ 68 · Jupyter Notebook · MIT · 推送 2026-08-17 · [GitHub](https://github.com/zarzouram/image_captioning_with_transformers) · 个人维护

**基于 Transformer 的图像描述生成课程项目（PyTorch 实现）**

哥德堡大学 LT2326 课程项目：基于 CPTR 架构的编码器-解码器 Transformer，用 ResNet101 特征图替代 ViT 初始化的图像嵌入，在 MS COCO 2017 上训练生成图像描述。推理使用大小为 5 的 beam search，输出 BLEU/METEOR/GLEU 指标及交叉注意力可视化。限制：需手动修改 PyTorch 1.8 的 functional.py 以返回逐头注意力；在约第 8 个 epoch 后出现早过拟合。提供数据集构建、训练、测试脚本与分析 notebook。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- CPTR 变体：ResNet101 特征图嵌入 + 2 层编码器/4 层解码器 Transformer
- beam search（size=5）生成描述，含 top-k 候选
- 交叉熵损失加 doubly stochastic attention 正则
- 提供 BLEU1-4、GLEU、METEOR 评测与注意力可视化 notebook

## 适用场景

- 学习图像描述任务的编码器-解码器 Transformer 实现细节
- 在 MS COCO 2017 上复现训练与推理流程
- 分析注意力可视化与模型过拟合行为

## 场景标签

`教程课程` `多模态` · 领域:学习与行业

## 证据(README 行号)

> L8: statistical NLP" Course. I used a transformer-based model to generate a caption
> L124: `code/inference_test.py` reads images from the test split and generats a description using beam search. The output

## 星数曲线

```mermaid
xychart-beta
    title "zarzouram/image_captioning_with_transformers 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 67 --> 69
    line [68, 68]
```

2026-10-18 68 → 2026-10-31 68（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `b2d9d37aed23` · [字段定义](../../DATASET.md)*

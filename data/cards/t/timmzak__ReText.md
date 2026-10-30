# timmzak/ReText

⭐ 21 · Python · 推送 2026-10-28 · [GitHub](https://github.com/timmzak/ReText) · [官网](https://arxiv.org/abs/2602.05785) · 组织维护

**用文本描述提升跨域行人重识别泛化的研究方法（WACV 2027）**

ReText 是一篇被 WACV 2027 接收的研究工作及其配套发布：训练阶段联合优化行人重识别、图文匹配与文本引导图像重建三项任务，用描述性自然语言标注为视觉特征补充跨域稳定的语义线索，使行人表征泛化到未见相机域而无需再训练；推理时仅使用动量图像编码器，不需要文本编码器与重建解码器。架构包含 ViT-Base 图像编码器、EMA 动量编码器、BERT-Base 文本编码器与图像解码器。仓库发布了对 CUHK03-NP、Market-1501、MSMT17、CUHK-SYSU、RandPerson 共五个数据集生成的文本标注（JSON，图像路径到描述的映射），以及基于 LLaVA-1.6-7B 微调的 VLM 权重和自建图像打标脚本（权重经 Git LFS 存储）。README 未给出安装命令；原始数据集图像不包含在发布中。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 训练联合三项任务：Re-ID、身份感知图文匹配、文本引导图像重建
- 推理仅用动量图像编码器，无需 caption、文本编码器或重建解码器
- 发布 5 个 Re-ID 数据集共 34 万余条生成的文本标注
- 发布微调 LLaVA-1.6-7B 权重及自有图像打标脚本

## 适用场景

- 跨相机域行人重识别研究中复现或对比该方法
- 为 Re-ID 数据集生成图像描述标注
- 用发布的 VLM 权重给自己的行人图像生成 caption

## 场景标签

 · 领域:计算机视觉/行人重识别

## 证据(README 行号)

> L20: ReText learns person representations that generalize to unseen camera domains without retraining. It uses descripti
> L22: The method combines multi-camera person Re-ID data with stylistically diverse single-camera data and jointly learns
> L40: The architecture comprises a ViT-Base image encoder, an exponential-moving-average (EMA) momentum image encoder, a 

## 星数曲线

```mermaid
xychart-beta
    title "timmzak/ReText 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 19 --> 22
    line [20, 21, 21]
```

2026-10-18 20 → 2026-10-30 21（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `0afe24bc746c` · [字段定义](../../DATASET.md)*

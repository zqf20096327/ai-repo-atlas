# Mark1708/beautify-old-photo

⭐ 14 · Jupyter Notebook · MIT · 推送 2026-05-29 · [GitHub](https://github.com/Mark1708/beautify-old-photo) · 个人维护

**老照片人脸修复与自动上色的研究 notebook（GFPGAN+DeOldify）**

在 Google Colab / Jupyter 中运行的单 notebook 实验项目：先用 GFPGAN 修复老照片中的人脸细节，再用 DeOldify 对原图与修复图自动上色，产出修复图、上色图与 colorized_output.zip。面向研究与教育用途，非生产服务。限制：依赖未固定版本，GFPGAN 与预训练模型来自外部 Colab 压缩包而非仓库内源码，上游 DeOldify 已归档，本仓库为保存快照，完整运行需网络与 GPU 运行时。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- GFPGAN 人脸修复 + DeOldify 自动上色两段流程
- 支持在 Google Colab 中按单元格复现，含示例输入照片
- 输出修复图、上色图与可下载的 zip 压缩包

## 适用场景

- 在 Colab 上修复并上色自己的家庭老照片
- 学习 GFPGAN/DeOldify 图像修复实验流程
- 对照仓库内示例照片查看修复前后效果

## 场景标签

`图像视频处理` `教程课程` · 领域:学习与行业

## 证据(README 行号)

> L24: - restore faces before colorization;
> L25: - colorize original and restored images;
> L34: - GFPGAN for real-world face restoration. In this repo it is loaded from the external Colab bundle, not from `requi

## 星数曲线

```mermaid
xychart-beta
    title "Mark1708/beautify-old-photo 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 13 --> 15
    line [14, 14]
```

2026-10-18 14 → 2026-10-31 14（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-31 · 置信度 mid · 依据 README sha `2d2a68b89e4d` · [字段定义](../../DATASET.md)*

# ramajoballester/UC3M-LP

⭐ 28 · Python · ODbL-1.0 · 推送 2026-10-25 · [GitHub](https://github.com/ramajoballester/UC3M-LP) · 组织维护

**西班牙车牌检测与识别标注数据集（UC3M-LP）**

UC3M-LP 是面向欧洲（西班牙）车牌检测与识别任务的开放标注图像数据集，供研究者与开发者训练和评测车牌检测、定位、字符分割及 OCR 算法。包含 1975 张图像、2547 辆不同车辆的 12757 个车牌字符，按 8:2 划分训练/测试集；每张车牌以两字母编码标注车牌类型（A–E 五类）与光照条件（日间/夜间）。数据集以自定义格式提供，附 Python 脚本可转换为 YOLO 格式，生成整图检测与裁剪区域识别两个版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-knowledge` | 知识聚合/清单类 |
| 许可风险 | `viral` | ODbL-1.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 1975 张图像 / 2547 辆车 / 12757 个车牌字符
- 车牌类型（A–E）与光照条件（日间 2185 / 夜间 362）双字母编码标注
- 提供脚本转换 YOLO 格式，输出检测与识别两个版本

## 适用场景

- 训练和评测西班牙车牌检测/识别算法
- 研究不同光照条件下的车牌 OCR
- 车辆监控、收费、交通分析等应用的数据基础

## 场景标签

`目标检测` `OCR` · 领域:感知与多模态

## 证据(README 行号)

> L3: UC3M-LP dataset is a comprehensive and open-source collection of annotated images for European (Spanish) license pla
> L5: It is the largest open-source dataset for European license plate detection and recognition and the first one ever de

## 星数曲线

```mermaid
xychart-beta
    title "ramajoballester/UC3M-LP 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 27 --> 29
    line [28, 28]
```

2026-10-18 28 → 2026-10-26 28（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 mid · 依据 README sha `78b480989f1e` · [字段定义](../../DATASET.md)*

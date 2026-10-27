# thavlik/machine-learning-portfolio

⭐ 50 · Python · Apache-2.0 · 推送 2026-04-12 · [GitHub](https://github.com/thavlik/machine-learning-portfolio) · [官网](https://thavlik.dev) · 个人维护

**深度学习研究者的医学数据 ML 实现作品集**

个人医学 AI 项目合集：包含已完成与进行中的实验（脑 CT 出血分类、EEG 动作检测、腹部 CT 肿瘤定位、fMRI 特征推断等）、自建数据集（神经外科手术视频、Doom/Quake 游戏数据）及若干工具（e-Shadowing 转录器、视频标注平台等）。实验通过 yaml 配置经 python3 src/main.py 运行，提供 Docker 复现环境；多数实验针对 11 GiB 显存显卡优化。仓库描述标注为 legacy。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 涵盖 CT/EEG/fMRI 等医学模态的模型实验（已完成 3 项、进行中 3 项）
- yaml 配置组合式实验，可用 Docker 复现运行
- 自建神经外科视频与游戏影像数据集
- 附相关文献清单（VAE/GAN/StyleGAN 等）

## 适用场景

- 复现医学影像分类/检测实验代码
- 参考 fMRI、EEG 建模的项目结构
- 获取神经外科视频与游戏数据集来源

## 场景标签

`科研工具` · 领域:学习与行业

## 证据(README 行号)

> L14: - RSNA Intracranial Hemorrhage Prediction: classification of brain CT scans by hemorrhage type
> L15: - Grasp-and-Lift EEG Detection: fine-grain detection of motor activity using EEG
> L16: - DeepLesion: localization of tumors on abdominal CT scans

## 星数曲线

```mermaid
xychart-beta
    title "thavlik/machine-learning-portfolio 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 49 --> 51
    line [50, 50]
```

2026-10-18 50 → 2026-10-27 50（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `4596b3ff13a0` · [字段定义](../../DATASET.md)*

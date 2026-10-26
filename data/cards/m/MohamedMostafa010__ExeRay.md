# MohamedMostafa010/ExeRay

⭐ 63 · Python · MIT · 推送 2026-03-30 · [GitHub](https://github.com/MohamedMostafa010/ExeRay) · 个人维护

**用机器学习检测 Windows 恶意可执行文件的工具**

基于 Python 与 scikit-learn 的静态 PE 文件恶意性分类工具：从可执行文件提取 50+ 特征（PE 结构、熵、导入表、字符串、VM 检测/反调试标记、可疑 API 模式），用 XGBoost + Random Forest 混合模型分类，输出置信度与威胁等级报告。提供含 10,925 恶意样本与 3,590 良性样本的数据集（MEGA 下载，仓库内不附带样本），采用欠采样平衡训练；论文在 IUGRC 2025 会议发表并随仓库提供 PDF。以 git clone 源码方式使用，包含特征提取、训练、预测三个脚本。README 说明了误报场景与阈值调整等缓解方法。

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

- 50+ 静态特征：PE 结构、熵、导入表、VM 检测/反调试标记
- XGBoost + Random Forest 混合分类，输出置信度与威胁等级
- 提供 14,515 样本（11.81 GB）数据集 MEGA 下载链接
- 配套论文在 IUGRC 2025 发表，PDF 随仓库提供

## 适用场景

- 对可疑 .exe 文件做快速静态恶意性分类
- 应急响应中辅助恶意文件初步筛查
- 用提供的数据集复现训练或做恶意软件检测研究

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L7: - Detect malicious `.exe` files using machine learning. Extracts **static features (entropy, imports, metadata) and 
> L66: - Hybrid AI detection **(XGBoost + Random Forest)**

## 星数曲线

```mermaid
xychart-beta
    title "MohamedMostafa010/ExeRay 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 62 --> 64
    line [63, 63]
```

2026-10-18 63 → 2026-10-26 63（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 mid · 依据 README sha `e505c9c46c81` · [字段定义](../../DATASET.md)*

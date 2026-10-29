# LollosoSi/bruxism-detector

⭐ 45 · C++ · GPL-3.0 · 推送 2026-09-25 · [GitHub](https://github.com/LollosoSi/bruxism-detector) · [官网](https://lollososi.github.io/bruxism-detector/) · 个人维护

**自制 Arduino EMG 设备：监测磨牙并给出生物反馈**

硬件加软件套件：通过电极读取咬肌 EMG 信号，运行 SVM 模型检测磨牙事件，并通过反馈信号提示使用者，同时记录数据以追踪诱发因素。包含核心模块、电池模块与 3D 打印外壳的组装指南、Android 应用、一键固件烧录；进阶路径支持 Python 手动训练 SVM、Processing 桌面日志与图表、Arduino IDE 手动编译及 C++ 定制阈值。声明非医疗设备，仅供教育/研究用途，检测输出尚待验证；佩戴电极时电路必须由电池供电。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- EMG 信号采集 + SVM 模型的磨牙检测
- 生物反馈提示与诱发因素追踪
- 提供 1-Click 固件烧录与 Android 应用，无需编程
- 支持 Python 重训练模型与 C++ 定制检测阈值

## 适用场景

- 我想自制设备监测夜磨牙并接受反馈训练
- 记录咬肌活动数据以找出磨牙诱因
- 教育/研究用途下复现和改进磨牙检测模型

## 场景标签

 · 领域:健康监测/自制硬件

## 证据(README 行号)

> L2: This small device + software suite helps you monitor jaw muscle activity and provide biofeedback to signal the user,
> L55: - Manual SVM model training via Python

## 星数曲线

```mermaid
xychart-beta
    title "LollosoSi/bruxism-detector 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 44 --> 46
    line [45, 45]
```

2026-10-18 45 → 2026-10-29 45（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `9ed2a519053c` · [字段定义](../../DATASET.md)*

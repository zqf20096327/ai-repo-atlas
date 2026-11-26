# m1ndl0ss/DuckyFence

⭐ 46 · Python · MIT · 推送 2026-11-17 · [GitHub](https://github.com/m1ndl0ss/DuckyFence) · 个人维护

**Windows 上检测 USB 击键注入攻击的行为检测工具**

在 Windows 上以击键间隔时序特征训练的 Random Forest 检测器：pynput 监听键盘输入，按 3 秒滑动窗口提取间隔统计特征（间隔数、均值、方差、变异系数、突发跨度），以 4 Hz 频率评分，连续两个恶意窗口即触发 BlockInput 阻断输入并弹出全屏锁屏，需输入随机挑战码解锁。面向担心 BadUSB/Rubber Ducky 注入的 Windows 用户。评估采用按打字者分组的交叉验证，自带数据采集与训练脚本。限制：需管理员权限运行，慢速拟人化注入（≥100 ms/键）不可分。

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

- 基于击键间隔时序的 Random Forest 检测，模型文件随仓库分发开箱可用
- 检测到攻击后 BlockInput 阻断输入并要求输入随机挑战码解锁
- 按打字者留出的交叉验证评估，含 v1 缺陷复盘与错误分析
- 提供数据集构建、训练、评估脚本，全部数字可用固定种子复现

## 适用场景

- 防范 Rubber Ducky 等 BadUSB 设备在机器上高速注入命令
- 在不可信物理环境下为 Windows 主机增加一层输入侧防护
- 复现击键动力学检测的实验结果并在此基础上继续研究

## 场景标签

`网络安全` · 领域:学习与行业

## 证据(README 行号)

> L3: Behavioural detection of USB keystroke injection on Windows: a Random Forest over inter-keystroke timing that blocks
> L9: When an attack is detected, system input is blocked (`BlockInput`), a fullscreen lockscreen takes over, and typing a
> L15: - 99.3% detection at 0.26% FPR under subject-held-out CV


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-26 · 置信度 high · 依据 README sha `d849467ec791` · [字段定义](../../DATASET.md)*

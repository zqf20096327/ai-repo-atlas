# huggingface/lerobot-humanoid-hardware

⭐ 39 · Python · Apache-2.0 · 推送 2026-08-27 · [GitHub](https://github.com/huggingface/lerobot-humanoid-hardware) · 组织维护

**LeRobot 人形机器人的开源硬件复现资料库**

HuggingFace 维护的 LeRobot Humanoid 双足平台硬件仓库：提供机械装配文档、Onshape CAD 源与导出的 STL 几何（75 个打印件）、电子接线与连接器映射、机器可读 BOM 与电机预装配调试工具（自包含 commission_motor.py，不依赖 robstride_toolkit）。当前范围仅覆盖双足平台，上半身硬件暂不包含。BOM 含 RobStride 电机、树莓派 5、IMU、CAN FD 适配器等，估算总价约 2,635.84 美元；控制运行时位于独立仓库 lerobot-humanoid-runtime。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | Apache-2.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- Onshape CAD 源与按左右腿/躯干组织的 75 个 STL 打印件
- 机器可读 BOM 与逐件成本估算（约 2,636 USD）
- 自包含电机调试脚本 commission_motor.py（CAN 通道向导式）
- 从采购、打印、电机调试到装配与上电的完整启动顺序文档

## 适用场景

- 按文档与 BOM 从零复现 LeRobot 人形机器人双足平台
- 采购 RobStride 电机、轴承与紧固件等部件
- 3D 打印 STL 零件并按指南装配与接线上电

## 场景标签

 · 领域:机器人硬件/具身智能

## 证据(README 行号)

> L3: Hardware repository for **LeRobot Humanoid**.
> L48: Runtime repository (robot model and control runtime) lives in:

## 星数曲线

```mermaid
xychart-beta
    title "huggingface/lerobot-humanoid-hardware 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 38 --> 40
    line [39, 39]
```

2026-10-18 39 → 2026-10-27 39（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 mid · 依据 README sha `984febb40f89` · [字段定义](../../DATASET.md)*

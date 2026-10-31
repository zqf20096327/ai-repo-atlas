# l1ve709/NeuroPace-RDNA

⭐ 15 · C++ · MIT · 推送 2026-10-14 · [GitHub](https://github.com/l1ve709/NeuroPace-RDNA) · 个人维护

**面向 AMD RDNA 显卡的预测性延迟管理工具，缓解游戏卡顿**

运行于 Windows 用户态（Ring-3）的系统优化软件，面向 AMD RDNA 架构显卡玩家：以 100Hz 采集 ETW 内核事件与 ADLX 硬件遥测（28 维特征、ONNX 推理）预测下一帧卡顿风险，通过线程迁移、GPU 调度优先级、中断队列重排与功耗/热限制调整进行预先缓解，并提供实时 Web 仪表盘。不读写游戏内存、不装内核驱动，声称兼容主流反作弊平台。支持 RDNA 1-3（ADLX SDK 兼容）显卡，Windows 64 位发布包可直接运行，需 Admin 权限以访问 ETW。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- ETW + ADLX 遥测融合，28 维特征 ONNX 推理预测卡顿风险
- 预emptive 缓解措施：线程迁移、GPU 优先级、中断重排、帧节奏平滑
- 纯用户态运行，零游戏内存访问、零内核驱动，决策留有审计日志
- 提供实时 Web 仪表盘与发布包 SHA-256 校验

## 适用场景

- 高帧率电竞游戏中消除周期性微卡顿
- 降低 AMD 显卡的温控降频与时钟波动
- 在兼容反作弊的前提下优化输入延迟与帧生成稳定性

## 场景标签

 · 领域:游戏/系统优化

## 证据(README 行号)

> L142: |**Prediction Engine**|Python/ONNX|28-feature inference, sub-ms latency, rolling window analysis|


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `c7bee2026a36` · [字段定义](../../DATASET.md)*

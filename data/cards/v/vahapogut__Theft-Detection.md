# vahapogut/Theft-Detection

⭐ 33 · Python · MIT · 推送 2026-10-10 · [GitHub](https://github.com/vahapogut/Theft-Detection) · [官网](https://theft-detection-dusky.vercel.app) · 个人维护

**面向零售的 AI 盗窃检测与安防事件审查系统**

基于 Python/FastAPI 后端与 Next.js 仪表盘的安防监控系统：对多路摄像头执行 YOLO 目标与姿态检测并独立跟踪，识别可疑活动、禁区闯入与滞留行为，生成带前后片段的 H.264 录像与快照供人工审查。支持隐私遮罩、事件筛选/归档/CSV 导出、保留期清理、管理员/操作员/查看者三种角色，以及邮件/Telegram 通知。README 明确声明模型输出本身不能判定盗窃发生，检测结果仅供人工复核。需 Python 3.11 与 Node.js 20.9+，CPU 可运行，CUDA 可选。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `high` | 编译与系统依赖俱全 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 多摄像头 YOLO 目标与姿态检测，独立跟踪与逐相机阈值/冷却配置
- 命名禁区与滞留区，含停留时长阈值
- 事件审查流程：状态/备注/归档保护/筛选/CSV 导出/前后片段录像
- 隐私遮罩在分析、直播与录制前应用；三角色权限与会话校验

## 适用场景

- 零售店铺监控可疑行为并留存证据供人工复核
- 划定禁区与滞留区并接收闯入/滞留告警
- 按日期、相机、类型筛选与导出安全事件

## 场景标签

`网络安全` `目标检测` · 领域:学习与行业

## 证据(README 行号)

> L10: - YOLO object and pose detection with independent tracking for each camera.
> L23: Detections flag suspicious activity for human review. Model output alone does not establish that theft occurred.

## 星数曲线

```mermaid
xychart-beta
    title "vahapogut/Theft-Detection 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 32 --> 34
    line [33, 33]
```

2026-10-18 33 → 2026-10-26 33（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `88ad738eaba6` · [字段定义](../../DATASET.md)*

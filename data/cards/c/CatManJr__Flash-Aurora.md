# CatManJr/Flash-Aurora

⭐ 36 · Python · MIT · 推送 2026-10-01 · [GitHub](https://github.com/CatManJr/Flash-Aurora) · [官网](https://catmanjr.github.io/Flash-Aurora-walkthrough/) · 个人维护

**地理空间基础模型（Microsoft Aurora 等）的推理与服务引擎**

面向 Microsoft Aurora 等地理空间基础模型的推理与服务引擎：输入分析立方体，输出 NetCDF 或 GeoTIFF。张量保持经纬度布局，采用形状专用 GPU 内核（CuTe DSL 短窗口注意力，N=144）、命名混合精度（默认 bf16_mixed@fp32）与作业级 GPU 调度器（每作业一 GPU，ZeroMQ 协调器填充空闲 worker），而非 LLM 服务循环。支持单预设跨双设备切分（DistributedConfig）与 ROI 裁剪导出。提供 9 个预设（ERA5/HRES/CAMS/wave 等）。限制：bf16@* 路径会损坏预测，非生产路径；wave 预设需手动放置 MARS 缓存。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- shape-specialized CuTe DSL 内核与命名混合精度（bf16_mixed@fp32 默认）
- 作业级 GPU 调度：一作业一 GPU，ZeroMQ 填充空闲 worker
- DistributedConfig 支持单预设跨双设备（encoder/backbone/decoder）切分
- 9 个预设覆盖 ERA5、HRES、CAMS、wave 等数据源

## 适用场景

- 对 Microsoft Aurora 系列气象模型做批量推理并导出 NetCDF/GeoTIFF
- 在有限 GPU 资源上调度多个地理空间模型作业
- 按感兴趣区域（ROI）裁剪导出，避免全量数据落盘

## 场景标签

`推理引擎` · 领域:训练与推理

## 证据(README 行号)

> L5: Inference and serving for Microsoft Aurora and other geospatial foundation models. A request takes an analysis cube 
> L51: Serving is one GPU per job. A ZeroMQ coordinator fills idle workers; it does not batch tokens inside one forward. S

## 星数曲线

```mermaid
xychart-beta
    title "CatManJr/Flash-Aurora 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 35 --> 37
    line [36, 36]
```

2026-10-18 36 → 2026-10-28 36（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-25 · 置信度 high · 依据 README sha `56d4de52906a` · [字段定义](../../DATASET.md)*

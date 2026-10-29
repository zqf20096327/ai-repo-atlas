# maxsitt/insect-detect

⭐ 71 · Python · GPL-3.0 · 推送 2026-09-03 · [GitHub](https://github.com/maxsitt/insect-detect) · [官网](https://maxsitt.github.io/insect-detect-docs/) · 个人维护

**太阳能 DIY 相机陷阱软件：设备端实时检测跟踪昆虫并拍摄**

运行于 Raspberry Pi Zero 2 W + Luxonis OAK-1 相机的野外昆虫监测相机陷阱软件：定制的昆虫检测模型与目标跟踪在 OAK 相机上实时运行，无需网络连接；检测触发时同步保存 3840x2160 MJPEG 高分辨率图像，并将时间戳、标签、置信度、跟踪 ID、边界框等元数据写入 csv。配套浏览器 Web 应用提供实时流、参数配置、数据下载、GPS 输入与终端访问；支持 Rclone 上传、低电量/磁盘/温度停止条件与 systemd 自启动。约 4.2 W 功耗，需配套 insect-detect-post 做后处理。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 定制检测模型与目标跟踪在 OAK 相机上实时运行，离线可用
- 检测触发捕获 3840x2160 高分辨率图像并记录逐帧元数据 csv
- 浏览器 Web 应用：实时流、配置、数据 zip 下载、集成终端
- Rclone 上传多种云存储后端、低电量/磁盘/温度自动停止与太阳能供电管理

## 适用场景

- 在野外远程地点长期自动监测并拍摄昆虫个体
- 田间通过手机/电脑连接热点实时查看检测流并调整配置
- 采集带边界框与跟踪信息的昆虫图像数据用于后续分析

## 场景标签

`目标检测` · 领域:感知与多模态

## 证据(README 行号)

> L12: The **Insect Detect** camera trap automatically detects and tracks insects in the field
> L34: - **On-device detection + tracking** - a custom insect detection model and

## 星数曲线

```mermaid
xychart-beta
    title "maxsitt/insect-detect 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 70 --> 72
    line [71, 71]
```

2026-10-18 71 → 2026-10-29 71（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `2a5ab2cd3733` · [字段定义](../../DATASET.md)*

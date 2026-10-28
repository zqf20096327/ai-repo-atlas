# OverStruck/deep-dream-maker

⭐ 55 · JavaScript · GPL-3.0 · 推送 2026-02-16 · [GitHub](https://github.com/OverStruck/deep-dream-maker) · 个人维护

**Google Deep Dream 的 Web 图形界面，免终端生成迷幻图像**

DeepDream Maker 是包裹 Google Deep Dream 的 Web 应用（Flask + React），让用户通过浏览器界面生成 Deep Dream 风格图像，无需使用终端或安装 caffe 等依赖，并可自定义生成参数。v2.0 版本改用 Docker 与 Docker Compose 部署，安装流程为 clone 仓库后 docker-compose build/up，随后访问 localhost:9993 使用。项目声明仍处于活跃开发中，部分功能可能存在问题。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `viral` | GPL-3.0 |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | `idea` | |

## 能力要点

- 浏览器界面替代终端操作生成 Deep Dream 图像
- 无需手动安装 caffe 等依赖
- 支持自定义 dream 生成参数
- Docker Compose 一键构建运行

## 适用场景

- 不熟悉命令行的用户制作 Deep Dream 风格图像
- 通过调参快速试验不同的 dream 效果

## 场景标签

`图像生成` · 领域:内容生成

## 证据(README 行号)

> L10: **DeepDream Maker** is a web application interface "wrapper" for Google's Deep Dream.
> L12: It allows you to easily dreamifty images without needing to use a terminal or install dependencies like caffe and p

## 星数曲线

```mermaid
xychart-beta
    title "OverStruck/deep-dream-maker 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 54 --> 56
    line [55, 55]
```

2026-10-18 55 → 2026-10-28 55（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-24 · 置信度 high · 依据 README sha `9d886ff8fa78` · [字段定义](../../DATASET.md)*

# trikko/etichetta

⭐ 23 · D · MIT · 推送 2026-10-06 · [GitHub](https://github.com/trikko/etichetta) · 个人维护

**D 语言编写的图像标注工具，面向 YOLO 数据集制作**

基于 D 语言开发的桌面图像标注应用，用于制作 YOLO 格式的标注数据；提供 3D 打印外设模型下载，含 HOWTO 与 AI 使用教程页面。Linux/Windows 提供 Snap 与 Windows 预编译包，也可从源码构建（需 DMD/LDC/GDC 等 D 编译器，Windows 另需 MSBuild 与 Windows SDK）；支持 GPU 加速（详见 ext 目录）。macOS 无原生支持，需通过 Docker 容器加 XQuartz 显示转发运行。MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 面向 YOLO 格式的图像标注桌面工具
- Linux Snap 与 Windows 预编译包，也可源码构建
- 支持 GPU 加速（见 ext/README.md）
- macOS 经 Docker + XQuartz 转发运行

## 适用场景

- 为 YOLO 目标检测训练制作图像标注
- 在 Linux/Windows 桌面上标注图像数据集

## 场景标签

 · 领域:计算机视觉/数据标注

## 证据(README 行号)

> L4: Etichetta is a project that aims to provide a simple and efficient way to annotate images.
> L30: To use GPU acceleration, read `ext/README.md`.

## 星数曲线

```mermaid
xychart-beta
    title "trikko/etichetta 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-29"]
    y-axis "stars" 22 --> 24
    line [23, 23]
```

2026-10-18 23 → 2026-10-29 23（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `d317486342df` · [字段定义](../../DATASET.md)*

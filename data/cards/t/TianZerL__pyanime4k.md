# TianZerL/pyanime4k

⭐ 121 · Python · MIT · 推送 2025-11-10 · [GitHub](https://github.com/TianZerL/pyanime4k) · 个人维护

**Python 封装 Anime4KCPP 的动漫图像超分辨率库**

基于 Anime4KCPP 的 Python 图像超分辨率库：导入 pyanime4k 后可直接对动漫图像执行放大处理，支持在可用时启用 OpenCL GPU 加速，也可手动创建 processor 进行逐级处理。提供打印支持模型的接口，并可结合 OpenCV、Pillow/numpy 处理图像数据。通过 pip 安装预编译包，或自行安装 OpenCL 开发库与 cmake 构建工具链从源码构建 wheel。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 封装 Anime4KCPP 的动漫图像超分辨率能力
- 支持 OpenCL GPU 加速（可用时启用）
- 提供手动 processor 的逐级放大方式
- 可与 OpenCV、Pillow/numpy 图像数据配合使用

## 适用场景

- 在 Python 管线中放大动漫风格图片
- 需要 OpenCL 加速的批量图像超分处理
- 结合 OpenCV/Pillow 工作流做图像后处理

## 场景标签

`图像视频处理` · 领域:感知与多模态

## 证据(README 行号)

> L3: PyAnime4K is a high performance anime image upscaler based on Anime4KCPP.
> L32: # with OpenCL acceleration, if possible

## 星数曲线

```mermaid
xychart-beta
    title "TianZerL/pyanime4k 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 120 --> 122
    line [121, 121]
```

2026-10-18 121 → 2026-10-28 121（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 high · 依据 README sha `ba3dc3fa9f38` · [字段定义](../../DATASET.md)*

# z-mahmud22/Dlib_Windows_Python3.x

⭐ 370 · BSL-1.0 · 推送 2026-02-24 · [GitHub](https://github.com/z-mahmud22/Dlib_Windows_Python3.x) · [官网](http://dlib.net/) · 个人维护

**Dlib 的 Windows x64 预编译 wheel 二进制分发仓库**

为 Python 3.7–3.14 与 Windows x64 提供机器学习/计算机视觉库 Dlib 的预编译 .whl 二进制文件，免去用户自行编译（通常需要 Visual Studio C++ 环境）。安装流程为按 Python 版本下载对应 wheel 后 pip install；另附从源码构建 Dlib 的步骤说明（安装 VS2022 C++ 工具链、clone 官方仓库、python -m build 生成 wheel）。覆盖 dlib 19.22 至 20.0 的多个版本。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | BSL-1.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 覆盖 Python 3.7–3.14 共 8 个版本的预编译 wheel
- 省去 Windows 上自行配置 C++ 编译环境的步骤
- 附从源码构建 Dlib 的完整步骤（VS2022 + python build）

## 适用场景

- Windows 上 pip 安装 Dlib 编译失败时直接使用预编译 wheel
- 在指定 Python 版本环境（venv/conda）中快速安装 Dlib
- 需要自行定制时按步骤从源码构建 Dlib

## 场景标签

 · 领域:计算机视觉/机器学习工具分发

## 证据(README 行号)

> L1: # Dlib compiled binary wheels for Python 3.7 - 3.14 on Windows and x64 CPUs
> L3: This repository contains the compiled binary (.whl) files for the Dlib library to install on Python versions 3.7 - 3

## 星数曲线

```mermaid
xychart-beta
    title "z-mahmud22/Dlib_Windows_Python3.x 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 369 --> 371
    line [370, 370]
```

2026-10-18 370 → 2026-10-25 370（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `1fa059e51b3f` · [字段定义](../../DATASET.md)*

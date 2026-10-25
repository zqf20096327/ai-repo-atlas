# trypear/pearai-master

⭐ 773 · Shell · 推送 2026-06-19 · [GitHub](https://github.com/trypear/pearai-master) · [官网](https://trypear.ai) · 组织维护

**聚合多个仓库的 AI 代码编辑器主仓库：VSCode 分支+AI 聊天**

PearAI 主仓库，汇总构成整个项目的各子仓库：pearai-app（VSCode 分支，承载编辑器功能）、pearai-submodule（Continue 分支，承载 AI 聊天功能）、落地页、文档与可选的半私有服务端（pearai-server，为不想自备 API key 的用户提供便利）。技术栈为 TypeScript/Electron，后端为 Python FastAPI + Supabase。构建需 Rust、Node.js 20.18.0、Python 3.11 与 C/C++ 工具链，通过 npm 安装依赖并从源码运行开发实例。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | — |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- VSCode 分支承载编辑器功能，Continue 分支承载 AI 聊天功能
- 可选半私有服务端，为不愿自备 API key 的用户提供便利
- TypeScript/Electron 客户端 + Python FastAPI/Supabase 后端
- 提供 Windows/macOS/Linux 三平台的源码构建说明

## 适用场景

- 参与 PearAI 代码编辑器的开发与贡献
- 从源码构建并本地运行 PearAI 编辑器
- 了解 PearAI 项目各子仓库的组成结构

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L7: - pearai-app: this is the VSCode fork part of PearAI and the outer directory of the project. It contains the bulk of
> L8: - pearai-submodule: this is the Continue fork part of PearAI and is a submodule of `pearai-app`. It contains the bul

## 星数曲线

```mermaid
xychart-beta
    title "trypear/pearai-master 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-25"]
    y-axis "stars" 772 --> 774
    line [773, 773]
```

2026-10-18 773 → 2026-10-25 773（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-21 · 置信度 high · 依据 README sha `9d6200cd84c6` · [字段定义](../../DATASET.md)*

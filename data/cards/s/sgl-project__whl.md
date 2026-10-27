# sgl-project/whl

⭐ 26 · HTML · MIT · 推送 2026-10-26 · [GitHub](https://github.com/sgl-project/whl) · [官网](https://docs.sglang.io/whl/) · 组织维护

**SGLang 预编译 wheel 的 PEP 503 包索引仓库**

存放 SGLang 各软件包预编译 wheel 的分发索引：仓库本身非源码仓库，而是 PEP 503 兼容的包索引页面，二进制文件托管于 GitHub Releases。支持按指定 CUDA 版本（如 cu129）安装 sglang-kernel 内核包，也提供 sglang 每日构建（nightly）的安装通道，通过 pip 的 --index-url 参数指向该索引使用。面向使用 SGLang 推理框架、需按 CUDA 环境安装预编译内核的开发者。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- PEP 503 兼容的 wheel 索引页面
- 支持按 CUDA 版本（cu129 等）安装 sglang-kernel
- 提供 sglang nightly 每日构建的 pip 安装通道
- 二进制 wheel 托管于 GitHub Releases

## 适用场景

- 按本机 CUDA 版本安装 SGLang 预编译内核包
- 获取 SGLang 的 nightly 每日构建版本
- 浏览 SGLang 各版本可用的 wheel 文件

## 场景标签

 · 领域:AI 基础设施/软件分发

## 证据(README 行号)

> L5: This repository hosts the **wheel index page** for SGLang packages. It is not the source code repository — it serves
> L11:   pip install sglang-kernel --index-url https://docs.sglang.io/whl/cu129

## 星数曲线

```mermaid
xychart-beta
    title "sgl-project/whl 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-27"]
    y-axis "stars" 25 --> 27
    line [26, 26]
```

2026-10-18 26 → 2026-10-27 26（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `5f66febf7b53` · [字段定义](../../DATASET.md)*

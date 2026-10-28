# AGiXT/python-sdk

⭐ 25 · Python · MIT · 推送 2026-01-26 · [GitHub](https://github.com/AGiXT/python-sdk) · [官网](http://agixt.com) · 组织维护

**AGiXT 平台的 Python SDK：通过 API 接入其 AI 自动化能力**

AGiXT Python SDK 仓库，封装 AGiXT AI 自动化平台的 API 接口：开发者通过 base_uri 与 API key 初始化客户端，调用平台的指令管理与任务执行等功能。AGiXT 平台本身定位为编排多 AI 提供商的自动化平台，含自适应记忆与插件系统，本仓库仅提供 Python 客户端库。安装方式为 pip install agixtsdk，另提供示例与测试的 Notebook。

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

- Python 客户端封装 AGiXT 平台 API
- pip install agixtsdk 安装
- 提供示例与测试 Notebook

## 适用场景

- 在 Python 项目中调用 AGiXT 平台的 agent 能力
- 编写脚本对接自部署的 AGiXT 服务

## 场景标签

`Agent 框架` · 领域:Agent 开发

## 证据(README 行号)

> L18: This repository is for the AGiXT SDK for Python.
> L31: base_uri = "http://localhost:7437"
> L34: ApiClient = AGiXTSDK(base_uri=base_uri, api_key=api_key)

## 星数曲线

```mermaid
xychart-beta
    title "AGiXT/python-sdk 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-28"]
    y-axis "stars" 24 --> 26
    line [25, 25]
```

2026-10-18 25 → 2026-10-28 25（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-27 · 置信度 mid · 依据 README sha `17104b9d2b5c` · [字段定义](../../DATASET.md)*

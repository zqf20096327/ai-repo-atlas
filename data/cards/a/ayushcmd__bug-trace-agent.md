# ayushcmd/bug-trace-agent

⭐ 4 · Python · Apache-2.0 · 推送 2026-11-21 · [GitHub](https://github.com/ayushcmd/bug-trace-agent) · [官网](https://ayushcmd.github.io/bug-trace-agent/) · 个人维护

**展示 bug 修复工作流（从失败测试到修复提案与人工审批）的演示项目**

一个以演示为目的的 bug 修复工作流项目，提供两种接口：无需安装即可在浏览器打开的静态页面，以及基于 FastAPI 的 Python 后端。后端流程为接收 bug 报告、用关键词匹配检索样例认证文件、运行 pytest 观察失败、临时应用预定义修复后再运行测试、等待审批。Gemini 与 Vertex AI 集成为实验性路径，默认演示模式是确定性的离线流程；审批为模拟，不创建 PR、合并或推送代码。运行历史保存在内存中，服务重启即丢失。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `none` | Apache-2.0 |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 浏览器演示无需安装、构建或 API key，刷新即重置
- FastAPI 后端含 /start_run、/status、/approve 等 5 个端点及交互式 API 文档
- Gemini（GEMINI_API_KEY）与 Vertex AI（GCP 项目+凭证路径）为实验性提供方选择路径
- DEMO_MODE=true 时可离线复现并运行 pytest 集成测试套件

## 适用场景

- 演示一个从失败测试到修复提案与人工审批的 bug 修复流程
- 在浏览器中跟踪示例认证 bug 的修复轨迹
- 本地运行 FastAPI 后端并调用其 API 体验审批工作流

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L3: A bug-fixing workflow demo with a static web interface and a Python API. Follow a sample authentication bug from fai
> L18: **The working demo is deterministic.** Gemini and Vertex AI integrations are experimental; they do not yet provide 
> L159: - Retrieval uses sample keyword matching, not vector search or repository-wide semantic indexing.

## 星数曲线

```mermaid
xychart-beta
    title "ayushcmd/bug-trace-agent 星数(近 3 点)"
    x-axis ["2026-11-13", "2026-11-21", "2026-11-24"]
    y-axis "stars" 2 --> 5
    line [3, 4, 4]
```

2026-11-13 3 → 2026-11-24 4（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 mid · 依据 README sha `8d808994c7f2` · [字段定义](../../DATASET.md)*

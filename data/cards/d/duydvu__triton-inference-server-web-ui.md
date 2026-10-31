# duydvu/triton-inference-server-web-ui

⭐ 21 · TypeScript · MIT · 推送 2026-07-25 · [GitHub](https://github.com/duydvu/triton-inference-server-web-ui) · 个人维护

**Triton Inference Server 的 Web 管理监控界面**

基于 Triton Inference Server HTTP API 构建的浏览器端管理工具（非 NVIDIA 官方产品）：列出模型仓库中的模型、加载/卸载模型、在线查看与编辑模型配置、监控模型指标。面向在 Triton 上开发测试模型的工程师，也可用于生产环境监控，但 README 提示不建议在生产中编辑模型配置，因服务器重启后修改会丢失。提供 Docker 镜像（需配置 API_URL 与可选认证头）与 Node.js >= 18 源码构建两种安装方式，MIT 许可。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `self-host` | docker 或自建部署 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 列出/加载/卸载模型仓库中的模型
- 在线查看与编辑模型配置
- 监控模型指标
- 支持 API 认证头连接受保护的 Triton 服务

## 适用场景

- 在浏览器中管理 Triton Inference Server 的模型仓库
- 开发调试阶段快速加载/卸载与调整模型配置
- 生产环境中查看模型运行指标

## 场景标签

 · 领域:推理服务运维/工具

## 证据(README 行号)

> L3: Manage and monitor your Triton Inference Server with a web browser. You can use this project to develop and test you
> L5: This project is built on top of Triton Inference Server HTTP API. It is not affiliated with NVIDIA.

## 星数曲线

```mermaid
xychart-beta
    title "duydvu/triton-inference-server-web-ui 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-31"]
    y-axis "stars" 20 --> 22
    line [21, 21]
```

2026-10-18 21 → 2026-10-31 21（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-28 · 置信度 high · 依据 README sha `f57c075a6321` · [字段定义](../../DATASET.md)*

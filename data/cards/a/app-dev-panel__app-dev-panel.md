# app-dev-panel/app-dev-panel

⭐ 92 · PHP · 推送 2026-09-03 · [GitHub](https://github.com/app-dev-panel/app-dev-panel) · [官网](https://app-dev-panel.github.io/app-dev-panel/) · 组织维护

**PHP 全框架通用的应用开发调试面板**

面向 PHP 开发者的统一调试面板：通过 Laravel、Symfony、Yii 3、Yii 2、Spiral 等框架适配器自动接入，提供 30 个数据收集器（日志、HTTP、SQL、事件、队列等）、28 个实时检查页面（路由、Git、Composer、测试、文件浏览等）与 40+ API 端点，前端为 React SPA。实时数据经 UDP + SSE 流式传输，Ingestion API（OpenAPI 3.1）可接收 Python、Node.js 等其他语言应用的调试数据。CLI 包可独立运行调试服务器。README 中未展示 AI 相关功能细节，仅仓库主题标签含 ai/llm。要求 PHP 8.4+。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `none` | — |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 30 个自动数据收集器，无需配置
- 28 个实时检查页面（路由/DB/Git/测试/命令执行等），无需 CLI 或重启
- 4 个框架适配器，任意 PSR 框架可接入
- 语言无关的 Ingestion API（OpenAPI 3.1），支持多应用调试

## 适用场景

- 在 Laravel/Symfony/Yii/Spiral 项目中查看日志、SQL、事件等运行时数据
- 从浏览器执行 Git 操作、Composer 包管理与测试套件
- 用一个面板同时调试多个微服务应用

## 场景标签

 · 领域:Web 开发/调试工具

## 证据(README 行号)

> L13: **30 collectors &middot; 28 live inspector pages &middot; 40+ API endpoints**
> L164: Any PHP App → Adapter → Kernel (30 collectors) → API (40+ endpoints) → React SPA

## 星数曲线

```mermaid
xychart-beta
    title "app-dev-panel/app-dev-panel 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-24"]
    y-axis "stars" 91 --> 93
    line [92, 92]
```

2026-10-18 92 → 2026-10-24 92（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 low · 依据 README sha `c96956cedf17` · [字段定义](../../DATASET.md)*

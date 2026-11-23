# gavinchen-520/agent-user-interaction

⭐ 5 · TypeScript · MIT · 推送 2026-10-20 · [GitHub](https://github.com/gavinchen-520/agent-user-interaction) · 个人维护 · 中文 README

**让编码 Agent 生成 HTML 页面向用户收集结构化确认的插件**

面向 OpenCode 编码 Agent 的 skill + 插件组合：模型在任务中途调用 create/update_html_session 等四个工具，生成自包含 HTML 页面在浏览器打开，用户点选、填写、确认后以 {kind, data, metadata} 结构化 JSON 回传给模型。页面运行在沙箱 iframe 中并配 CSP，禁止网络请求与宿主访问；会话一次性，有 TTL 与页面版本机制。需 Bun >= 1.3.14 与 OpenCode，skill 整目录复制，插件支持 V1/V2 两套 API，V1 需构建。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-ecosystem` | LLM/agent 周边工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `None` |  |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 四个工具调用完成页面创建、提交等待、换页与会话结束
- sandbox iframe + 独立 CSP 的安全模型，禁止网络请求与原生表单提交
- 页面版本递增与 409 STALE_PAGE，wrapper 轮询自动刷新
- 提交结果为可序列化结构化数据，直接进入下一步工具调用

## 适用场景

- 部署、删除等有副作用的操作前让用户确认影响面
- 一次填完多字段配置项并得到结构化结果
- 代码评审/审批场景展示 diff 并收集批准或驳回原因
- 多步骤流程中同会话内换页收集逐步确认

## 场景标签

`编码 Agent` · 领域:编码与开发

## 证据(README 行号)

> L9: AUI 是一套面向编码 Agent 的 **HTML 交互能力**：模型在任务中途临时生成一个自包含的 HTML 页面，浏览器里打开，用户点选、填写、确认，结构化数据再回传给模型，页面用完即弃。
> L40: 页面运行在 `sandbox="allow-scripts"` 的 iframe 里，配独立 CSP：不能发网络请求、不能读文件、不能访问宿主 API、不能弹窗。安全边界由插件兜底，模型不需要（也不应该）自己实现传输层。
> L150: 2. `create_html_session`、`wait_html_submission`、`update_html_session`、`end_html_session` 四个工具可被模型调用；

## 星数曲线

```mermaid
xychart-beta
    title "gavinchen-520/agent-user-interaction 星数(近 2 点)"
    x-axis ["2026-10-23", "2026-11-23"]
    y-axis "stars" 4 --> 6
    line [5, 5]
```

2026-10-23 5 → 2026-11-23 5（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-11-21 · 置信度 high · 依据 README sha `eeae2bc39614` · [字段定义](../../DATASET.md)*

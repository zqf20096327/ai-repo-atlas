# chen647208/hongyue-creation

⭐ 32 · TypeScript · AGPL-3.0 · 推送 2026-10-29 · [GitHub](https://github.com/chen647208/hongyue-creation) · [官网](https://chen647208.github.io/hongyue-creation/) · 个人维护 · 中文 README

**本地优先的小说创作桌面应用：纯写作完整可用，AI 为增强层**

Electron + React + TypeScript 桌面写作工具，覆盖灵感、世界构建、角色、大纲到成稿导出的流程，数据存本地 SQLite。禁用全部插件与 AI 后纯写作完整可用。AI 部分：主进程网关托管 API Key，支持 Anthropic/Gemini/OpenAI 兼容（含 Ollama）等适配器；Agent 循环带工具调用与三档审批，写操作不静默应用；支持逐条目 AES-256-GCM 加密、插件沙箱与 WebDAV/S3 同步。发布版为开箱即用安装包，Node 仅源码运行需要。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `viral` | AGPL-3.0 |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | local-ok | 支持本地模型 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 禁用全部插件与 AI 后纯写作完整可用（本地优先）
- 四类 AI 适配器（Anthropic/Gemini/OpenAI 兼容含 Ollama/Responses），主进程网关托管 Key
- Agent 循环：工具调用 + 三档审批 + jsonl 留痕回放，写操作不静默应用
- 逐条目 AES-256-GCM 加密与插件沙箱（签名校验 + 权限默认拒绝）

## 适用场景

- 在本地离线环境完成从灵感到成稿导出的小说创作
- 需要时可配置 AI 渠道辅助生成书名、大纲与改写
- 用 Build Profile 与多格式导出（ePub/DOCX/PDF 等）生成交付稿

## 场景标签

`AI 写作` `知识库管理` · 领域:内容生成

## 证据(README 行号)

> L5: 红月创作是一款 Electron + React + TypeScript 桌面应用，覆盖从灵感、设定、大纲到成稿导出的完整创作流程。项目数据保存在本地，经 SQLite 单一事务管线与开放格式流转；禁用全部插件与 AI 后，纯写作
> L23: 4. 需要 AI 时，在模型设置中配置渠道密钥；未配置时纯手写不受影响。
> L62: - 插件状态面板与装配树查看器、发行档（完整 / 网文 / 严肃文学 / 纯写作，minimal 即时禁用全部 AI）；MIT SDK 独立发行。

## 星数曲线

```mermaid
xychart-beta
    title "chen647208/hongyue-creation 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-30"]
    y-axis "stars" 31 --> 33
    line [32, 32]
```

2026-10-18 32 → 2026-10-30 32（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `4436cbed256e` · [字段定义](../../DATASET.md)*

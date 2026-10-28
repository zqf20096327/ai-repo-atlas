# agent-labs-dev/fastbrowse

⭐ 120 · Python · MIT · 推送 2026-10-27 · [GitHub](https://github.com/agent-labs-dev/fastbrowse) · 组织维护

**浏览器 Agent：选择模型 Jev 逐步操作页面，LLM 规划并输出带引文引用的回答**

fastbrowse 是一个本地或云端浏览器中运行任务的 CLI 工具：它把页面索引为候选控件，由选择模型 Jev 逐个挑选动作（不生成页面上不存在的选择器），LLM 负责阅读与规划；最终返回引用页面原文的回答或 schema 校验的数据。凭据、授权与支出由代码控制：`--secret` 作用域密钥、`--authorize` 提交门、`--max-dollars` 预算上限。默认使用 Browser Use Cloud 浏览器，也可 `--local` 用本地 Chrome 或通过 CDP 接管已有浏览器/Electron 窗口。需 uv，Python 3.13+，经 PyPI 分发。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | locked-api |  |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `medium` | 含编译或系统依赖之一 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 选择模型 Jev 从页面已索引控件中挑选动作，不生成虚构选择器
- 回答中的事实声明引用页面原文，支持 schema 校验数据输出
- --secret/--bitwarden 作用域凭据与 --authorize 提交授权门、--max-dollars 支出上限
- 支持本地 Chrome、Browser Use Cloud、CDP 接管已开浏览器与 Electron 应用

## 适用场景

- 用自然语言让 Agent 在网页上完成登录、下单、填表等任务
- 从网页提取有原文出处引用的事实性回答
- 在已登录的浏览器配置文件或 Bitwarden 密码库下代操作站点

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L5: Run browser tasks locally or in a cloud browser. Jev chooses from indexed page controls; fastbrowse returns
> L15: fastbrowse indexes the page into candidates and has Jev, a choice model, **pick one**, so it cannot click
> L41: - **LLM agents that generate actions** (the hosted Browser Use agent and similar): Jev picks each action from the c

## 星数曲线

```mermaid
xychart-beta
    title "agent-labs-dev/fastbrowse 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-27", "2026-10-28"]
    y-axis "stars" 118 --> 121
    line [120, 119, 120]
```

2026-10-18 120 → 2026-10-28 120（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-23 · 置信度 mid · 依据 README sha `0ba07023bfe3` · [字段定义](../../DATASET.md)*

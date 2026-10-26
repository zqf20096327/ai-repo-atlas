# nicedreamzapp/browser-agent

⭐ 29 · Python · MIT · 推送 2026-10-25 · [GitHub](https://github.com/nicedreamzapp/browser-agent) · [官网](https://youtu.be/SIuMNa2k6Wc) · 组织维护

**本地浏览器 AI 代理与共享浏览器安全代理（Apple Silicon/MLX）**

两件配套工具：一是运行在本机 MLX 模型上的浏览器代理（agent.py），用自然语言下达任务，在真实 Brave 浏览器与 shell 中执行；二是 broker，一个占用 CDP 9222 调试端口的本地代理，为每个代理分配独占标签页租约，识别用户正在操作的页面并阻止代理干扰。代理部分需 Apple Silicon（建议 32GB 统一内存）、Python 3.12+ 及 claude-code-local 的 MLX 服务器；broker 可与任何 CDP 工具（Playwright 等）配合使用。声称处理跨域 iframe、Shadow DOM、ProseMirror；限制：跨站 frame 内验证码点击仅计为焦点活动。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-native` | 本体是模型或模型工具 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `desktop` | 安装包/桌面程序 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- 本地 MLX 模型驱动，不调用云端 API
- broker 独占标签页租约与人类活动检测（isTrusted 事件、20 秒静默窗口）
- 五条规则（一任务一标签页、先看后点、察觉人类介入等）在代理与 broker 两侧均有测试
- broker 兼容任意 CDP 客户端（Playwright、chrome-devtools-mcp 等）

## 适用场景

- 在已登录的真实浏览器中让本地 AI 代为完成网页任务
- 多个浏览器代理并行时避免互相抢占标签页
- 人在代理操作的页面上手动输入时保护其工作不被覆盖

## 场景标签

`浏览器自动化` · 领域:效率与自动化

## 证据(README 行号)

> L21: |🌐|**The agent** (`agent.py`)|You type a task in plain English. A model running on your own Mac picks the steps, an
> L121: **2. The agent.** Needs Apple Silicon (32 GB+ unified memory recommended), Python 3.12+, and the local MLX server 

## 星数曲线

```mermaid
xychart-beta
    title "nicedreamzapp/browser-agent 星数(近 2 点)"
    x-axis ["2026-10-18", "2026-10-26"]
    y-axis "stars" 28 --> 30
    line [29, 29]
```

2026-10-18 29 → 2026-10-26 29（+0）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `1860a81c29a7` · [字段定义](../../DATASET.md)*

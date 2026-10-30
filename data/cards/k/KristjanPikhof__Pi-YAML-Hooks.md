# KristjanPikhof/Pi-YAML-Hooks

⭐ 17 · TypeScript · MIT · 推送 2026-09-26 · [GitHub](https://github.com/KristjanPikhof/Pi-YAML-Hooks) · [官网](https://npmjs.com/package/pi-yaml-hooks) · 个人维护

**为 Pi/OMP 编码 agent 提供 YAML 钩子：守卫工具调用与自动化会话事件**

面向 Pi 与 Oh My Pi（OMP）两个宿主的 YAML 钩子运行器，用同一包和同一钩子格式接入。可监听 user.prompt.submit、tool.before/after、file.changed、session.idle 等事件，执行 bash、tool、notify、confirm、setStatus 等动作；bash 动作通过 stdin JSON 与 PI_* 环境变量接收上下文，tool.before 钩子可用退出码 2 阻断工具调用或改写参数。项目级钩子需 /hooks-trust 显式信任后才加载，导入其他 YAML 需环境变量开启。要求 macOS/Linux、Node.js>=22.19.0、bash，不支持 Windows。

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

- 同一包与钩子格式同时支持 Pi 与 OMP 两个宿主
- tool.before 钩子可阻断工具调用或改写其参数
- 事件覆盖 prompt 提交、工具调用前后、文件变更与会话生命周期
- 项目钩子基于信任锚点加载，导入需显式环境开关

## 适用场景

- 在编码 agent 执行危险工具调用前加确认或拦截
- 文件变更或会话空闲时自动运行脚本与通知
- 为提交的 prompt 动态注入系统上下文

## 场景标签

 · 领域:开发者工具/编码 agent 扩展

## 证据(README 行号)

> L3: `pi-yaml-hooks` runs YAML-configured hooks in Pi and Oh My Pi (OMP). Use it to guard tool calls, react to file and s
> L51: |Events|`user.prompt.submit`, `tool.before.*`, `tool.after.*`, `file.changed`, `session.created`, `session.idle`, `

## 星数曲线

```mermaid
xychart-beta
    title "KristjanPikhof/Pi-YAML-Hooks 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-19", "2026-10-30"]
    y-axis "stars" 15 --> 18
    line [16, 17, 17]
```

2026-10-18 16 → 2026-10-30 17（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-30 · 置信度 high · 依据 README sha `940dc589b60e` · [字段定义](../../DATASET.md)*

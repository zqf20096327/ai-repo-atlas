# damiansire/web-ar-molecule-lab

⭐ 28 · TypeScript · MIT · 推送 2026-10-06 · [GitHub](https://github.com/damiansire/web-ar-molecule-lab) · [官网](https://damiansire.github.io/web-ar-molecule-lab/) · 个人维护

**浏览器化学实验游戏：语音与手部追踪拼合原子发现分子**

在浏览器中运行的化学教育游戏：用户说出原子名或从面板选取原子，用手部追踪将元素投入炼金坩埚，按配方生成真实分子（9 种元素、16 种一级分子、4 种炼金树化合物），产物存入可持久化库存并可作为新原料组合出更复杂化合物。手部追踪基于 MediaPipe Tasks Vision 在 Web Worker 中本地运行，语音用 Web Speech API，支持西/英/意/葡四种语言；无摄像头时可全程用键盘鼠标游玩。视频不离开设备，首次调用摄像头前有知情提示。

## 筛选速览

| 维度 | 判定 | 备注 |
|---|---|---|
| AI 角色 | `ai-enhanced` | 去掉 AI 部分产品仍成立 |
| 许可风险 | `permissive` | MIT |
| 部署形态 | `library` | 以包/库形式分发 |
| 模型依赖 | — | README 未给出锁定关系 |
| 硬件要求 | — | 无带数字的原话,不猜 |
| 安装摩擦 | `low` | 无编译、无系统依赖或容器化 |
| 成熟度 | — | 结构信号不足 |

## 能力要点

- MediaPipe 手部追踪在 Web Worker 中本地推理，不阻塞渲染循环
- 9 种元素、16 种一级分子与 4 种可层层组合的炼金树化合物
- 界面与语音识别支持西/英/意/葡四语
- 无摄像头模式下可全程键盘/鼠标游玩，库存跨刷新持久化

## 适用场景

- 在浏览器里用手势和语音拼合原子学习化学反应
- 逐步组合中间产物探索更复杂的化合物树
- 无需安装任何软件的课堂化学演示

## 场景标签

 · 领域:教育/化学游戏

## 证据(README 行号)

> L7: **Combine atoms with your hands and your voice.** A chemistry lab in your browser:
> L84: - **Hand tracking** via MediaPipe Tasks Vision,
> L35: Click **“No camera? Play with keyboard/mouse”** on the start screen to skip the camera

## 星数曲线

```mermaid
xychart-beta
    title "damiansire/web-ar-molecule-lab 星数(近 3 点)"
    x-axis ["2026-10-18", "2026-10-28", "2026-10-31"]
    y-axis "stars" 26 --> 29
    line [27, 28, 28]
```

2026-10-18 27 → 2026-10-31 28（+1）


---
*卡片 v1 · prompt 1.4 · 生成 2026-10-26 · 置信度 high · 依据 README sha `653f1a980641` · [字段定义](../../DATASET.md)*
